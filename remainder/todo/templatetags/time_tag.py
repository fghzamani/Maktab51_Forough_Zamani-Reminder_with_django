from django import template
from django.utils import timezone
register = template.Library()



@register.simple_tag()
def remaining_time(deadline):

    """
    calculate the remianing time untill the deadline of task
    """
    residual_time = deadline - timezone.now()
    return residual_time

@register.filter()
def captilizer_first_letter(value):

    """
    make first letter of task titles Upper case
    """
    first_letter = value[0]
    others = value[1:]
    return first_letter.upper()+others