from django import template

register = template.Library()

@register.filter    #함수앞에 @~(에너테이션) 적용하여 템플릿에서 필터로 사용가능
def sub(value, arg):
    return value -arg