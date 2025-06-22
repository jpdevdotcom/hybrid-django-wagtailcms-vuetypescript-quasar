from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField

class HomePage(Page):
    body = RichTextField(blank = True);
    
    content_panels = Page.content_panels + [FieldPanel('body')]
    
class ArticlePage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
    
    api_fields = [
        APIField('intro'),
        APIField('body'),
    ]
    