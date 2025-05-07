from django.urls import path
# Import all necessary views
from .views import (
    home,
    course_list,
    course_detail,
    add_course,
    delete_course,
    update_lesson,
    add_lesson,
    assignment_list,
    add_assignment,
    submit_assignment,
    forum_list,
    create_forum,
    forum_detail,
    quiz_list,
    quiz_detail,
)

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('courses/', course_list, name='course_list'),  # Course list
    path('courses/<int:course_id>/', course_detail, name='course_detail'),  # Course detail
    path('courses/add/', add_course, name='add_course'),  # Add course
    path('courses/<int:course_id>/delete/', delete_course, name='delete_course'),  # Delete course
    path('lessons/<int:lesson_id>/update/', update_lesson, name='update_lesson'),  # Update lesson
    path('courses/<int:course_id>/lessons/add/', add_lesson, name='add_lesson'),  # Add lesson
    path('courses/<int:course_id>/assignments/', assignment_list, name='assignment_list'),  # Assignment list
    path('courses/<int:course_id>/assignments/add/', add_assignment, name='add_assignment'),  # Add assignment
    path('assignments/<int:assignment_id>/submit/', submit_assignment, name='submit_assignment'),  # Submit assignment

    # Forum-related URLs
    path('courses/<int:course_id>/forums/', forum_list, name='forum_list'),
    path('courses/<int:course_id>/forums/create/', create_forum, name='create_forum'),
    path('forums/<int:forum_id>/', forum_detail, name='forum_detail'),

    # Quiz-related URLs
    path('courses/<int:course_id>/quizzes/', quiz_list, name='quiz_list'),
    path('quizzes/<int:quiz_id>/', quiz_detail, name='quiz_detail'),
]
