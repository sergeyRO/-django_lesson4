from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        arr_main = list()
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            #form.cleaned_data
            if form.cleaned_data:
                if form.cleaned_data['is_main'] and (form.cleaned_data['is_main'] in arr_main):
            # # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # # таким образом объект не будет сохранен,
            # # а пользователю выведется соответствующее сообщение об ошибке
                    raise ValidationError("РАЗДЕЛ МОЖЕТ БЫТЬ ТОЛЬКО ОДИН ОСНОВНОЙ")
                else:
                    arr_main.append(form.cleaned_data['is_main'])
        print(arr_main)
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    verbose_name = 'Тематический раздел'
    verbose_name_plural = 'Тематические разделы'
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_filter = ['published_at']
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

# @admin.register(ChapterMain)
# class ChapterMainAdmin(admin.ModelAdmin):
#     pass