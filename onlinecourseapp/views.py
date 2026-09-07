from django.shortcuts import render, get_object_or_404
from .models import Course, Question, Choice, Submission


def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(
        request,
        'onlinecourseapp/course_details_bootstrap.html',
        {'course': course}
    )


def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        score = 0
        total_grade = 0

        for question in Question.objects.filter(course=course):
            total_grade += question.grade

            selected_choice_id = request.POST.get(
                f'question_{question.id}'
            )

            if selected_choice_id:
                choice = get_object_or_404(
                    Choice,
                    id=selected_choice_id,
                    question=question
                )

                Submission.objects.create(
                    question=question,
                    choice=choice
                )

                if choice.is_correct:
                    score += question.grade

        return render(
            request,
            'onlinecourseapp/exam_result.html',
            {
                'course': course,
                'score': score,
                'total_grade': total_grade,
            }
        )

    return render(
        request,
        'onlinecourseapp/exam.html',
        {'course': course}
    )


def show_exam_result(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    submissions = Submission.objects.filter(
        question__course=course
    )

    score = 0
    total_grade = 0

    questions = Question.objects.filter(course=course)

    for question in questions:
        total_grade += question.grade

        submission = submissions.filter(
            question=question
        ).first()

        if submission and submission.choice.is_correct:
            score += question.grade

    return render(
        request,
        'onlinecourseapp/exam_result.html',
        {
            'course': course,
            'score': score,
            'total_grade': total_grade,
        }
    )

def exam(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(
        request,
        'onlinecourseapp/exam.html',
        {'course': course}
    )
