# Daily Deals & Guides

Welcome to your automated daily content site.

## Latest Articles
{% for file in site.pages %}
{% if file.path contains "articles" %}
- [{{ file.title }}]({{ file.url }})
{% endif %}
{% endfor %}
