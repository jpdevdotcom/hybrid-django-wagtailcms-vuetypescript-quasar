from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    pass

class ArticlePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
