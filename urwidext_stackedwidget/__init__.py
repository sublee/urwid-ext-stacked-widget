
__author__ = 'Sumin Byeon'
__version__ = '0.1.0'

import urwid

class StackedWidget(urwid.Widget):
    """A widget container that presents one child widget at a time."""

    #: A list containing all widgets
    widgets = []

    #: An index of the current widget
    current = 0

    def add_widget(self, widget):
        """Appends a widget at the end of the list."""
        self.widgets.append(widget)

    def insert_widget(self, index, widget):
        """Inserts a widget at a given index."""
        self.widgets.insert(index, widget)

    def show_widget(self, index):
        assert 0 <= index < len(self.widgets)
        self.current = index
        self._invalidate()

    @property
    def widget_count(self):
        """The function name is pretty much self-explanatory."""
        return len(self.widgets)

    @property
    def current_widget(self):
        """Returns a widget that is currently being rendered. If the widget
        list is empty, it returns None."""
        if self.widget_count > 0:
            return self.widgets[self.current]
        else:
            return None

    def render(self, size, focus=False):
        assert self.current_widget is not None

        return self.current_widget.render(size, focus)
