from django import template

register = template.Library()


@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__


@register.filter
def input_class(bound_filter):
    css_class = ''

    if bound_filter.form.is_bound:
        if bound_filter.errors:
            css_class = 'is-invalid'
        elif field_type(bound_filter) != 'PasswordInput':
            css_class = 'is-valid'

    return f'form-control {css_class}'
