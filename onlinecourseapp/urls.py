

from django.urls import path
from . import views

app_name = 'onlinecourseapp'

urlpatterns = [
    path(
        'course/<int:course_id>/',
        views.course_details,
        name='course_details'
    ),

    path(
        'course/<int:course_id>/exam/',
        views.exam,
        name='exam'
    ),

    # Required submit path
    path(
        '<int:course_id>/submit/',
        views.submit,
        name='submit'
    ),

    # Required exam result path
    path(
        '<int:course_id>/exam_result/<int:submission_id>/',
        views.show_exam_result,
        name='show_exam_result'
    ),

    # Existing route kept for the exam form
    path(
        'course/<int:course_id>/submit/',
        views.submit,
        name='course_submit'
    ),

    path(
        'course/<int:course_id>/exam_result/<int:submission_id>/',
        views.show_exam_result,
        name='course_exam_result'
    ),
]