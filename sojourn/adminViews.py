import flask

from railz.base import BaseView, Route
from railz.models import *
from railz.adminViews import requireRole

class AdminRootView(BaseView):
    
    @Route('/admin/')
    def get(self):
        user = AdminUser.get()
        if user is None:
            return flask.redirect('/railz/login/')
        else:
            requireRole('admin')
            return flask.render_template('admin/adminRoot.jinja2')