from django.contrib import admin
from .models import Course
from .models import Lesson
from .models import Instructor
from .models import Question
from .models import Choice
from .models import Submission
from .models import Enrollment


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
