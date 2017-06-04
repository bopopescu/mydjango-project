from django import template
from django.db.models import Count
register = template.Library()

from ..models import Post


@register.simple_tag() #정량화된 포스트의 정보들을 갖고옴
def total_posts():
    return Post.published.count()

#db에 있는 글을 링크형태로 가져오는 것
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}
#제일 많은 수의 코멘트부터 가져오는 것
@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

from django.utils.safestring import mark_safe
import markdown

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))