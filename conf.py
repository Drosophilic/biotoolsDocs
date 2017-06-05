html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }


def setup(app):
    app.add_stylesheet('my_theme.css')
