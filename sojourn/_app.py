import railz

import railz.commonSubviews
import railz.adminViews
import railz.templating

import sojourn.clientViews
import sojourn.adminViews

APP = railz.makeApp(
    'sojourn._app',
    viewModules=[
        sojourn.clientViews, 
        sojourn.adminViews, 
        railz.adminViews,
    ],
    templatingModules=[
        railz.templating,
    ],
    templateDirs=[
        'templates',
        'lib/railz/templates',
    ],
    subviewModules=[
        railz.commonSubviews,
    ],
)