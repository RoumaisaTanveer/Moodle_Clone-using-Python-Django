# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, Assignment, Submission,Quiz,Forum,Question,Post
from django.contrib import messages

def home(request):
    return render(request, 'core/home.html')
    


#@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'core/course_list.html', {'courses': courses})

#@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all()
    assignments = course.assignments.all()
    return render(request, 'core/course_detail.html', {'course': course, 'lessons': lessons, 'assignments': assignments})

#@login_required
def add_course(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Course.objects.create(title=title, description=description)
        return redirect('course_list')
    return render(request, 'core/add_course.html')

#@login_required
def add_lesson(request, course_id):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        course = get_object_or_404(Course, id=course_id)
        Lesson.objects.create(course=course, title=title, content=content)
        return redirect('course_detail', course_id=course.id)
    return render(request, 'core/add_lesson.html', {'course_id': course_id})

#@login_required
def assignment_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    assignments = course.assignments.all()
    return render(request, 'core/assignment_list.html', {'course': course, 'assignments': assignments})

#@login_required
def add_assignment(request, course_id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        course = get_object_or_404(Course, id=course_id)
        Assignment.objects.create(course=course, title=title, description=description, due_date=due_date)
        return redirect('assignment_list', course_id=course.id)
    return render(request, 'core/add_assignment.html', {'course_id': course_id})

#@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        content = request.POST['content']
        Submission.objects.create(assignment=assignment, student=request.user, content=content)
        return redirect('assignment_list', course_id=assignment.course.id)
    return render(request, 'core/submit_assignment.html', {'assignment': assignment})

#@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'core/delete_course.html', {'course': course})

#@login_required
def update_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == 'POST':
        lesson.title = request.POST['title']
        lesson.content = request.POST['content']
        lesson.save()
        return redirect('course_detail', course_id=lesson.course.id)
    return render(request, 'core/update_lesson.html', {'lesson': lesson})
#@login_required
def forum_list(request, course_id):
    # Get the course object
    course = get_object_or_404(Course, id=course_id)
    
    # Filter forums related to the course
    forums = Forum.objects.filter(course=course)  # Assuming there's a foreign key relationship
    
    context = {'forums': forums, 'course': course}
    return render(request, 'forums/forum_list.html', context)


#@login_required
def create_forum(request, course_id):
    if request.method == 'POST':
        title = request.POST['title']
        course = get_object_or_404(Course, id=course_id)
        Forum.objects.create(title=title, course=course)
        return redirect('forum_list', course_id=course.id)
    return render(request, 'forums/create_forum.html')

#@login_required
def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    posts = Post.objects.filter(forum=forum)
    if request.method == 'POST':
        content = request.POST['content']
        Post.objects.create(forum=forum, user=request.user, content=content)
    context = {'forum': forum, 'posts': posts}
    return render(request, 'forum_detail.html', context)


#@login_required
def quiz_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = Quiz.objects.filter(course=course)
    return render(request, 'quizzes/quiz_list.html', {'course': course, 'quizzes': quizzes})

#@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)  # Fetch the quiz, return 404 if not found
    questions = Question.objects.filter(quiz=quiz)  # Get questions associated with the quiz

    if request.method == 'POST':
        score = 0
        for question in questions:
            user_answer = request.POST.get(str(question.id), "")  # Get user's answer
            if user_answer == question.correct_answer:  # Check if the answer is correct
                score += 1
        # After calculating the score, you can redirect to a results page
        return render(request, 'quizzes/quiz_result.html', {'score': score, 'total': len(questions)})

    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz, 'questions': questions})  # Render quiz details
