from django.contrib import admin
from .models import (
    Instructor,
    Course,
    Lesson,
    Question,
    Choice,
    Submission,
    Enrollment,
)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'course', 'lesson', 'grade')
    list_filter = ('course', 'lesson')
    search_fields = ('question_text',)
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('course',)
    search_fields = ('title',)
    inlines = [QuestionInline]


admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)