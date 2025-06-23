from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

class HomePage(Page):
    body = RichTextField(blank = True);
    
    content_panels = Page.content_panels + [FieldPanel('body')]
    
class ArticlePage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname='full title')),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('content'),
    ]
    
    api_fields = [
        APIField('intro'),
        APIField('body'),
        APIField('content'),
    ]
    