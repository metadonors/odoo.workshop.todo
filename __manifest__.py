{
    'name': 'Applicazione TODO',
    'description': 'Gestisci i tuoi TODO',
    'author': 'Fabrizio Arzeni',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/todo_model_acl.xml',
        'views/todo_menu.xml',
        'views/todo_views.xml',
    ]
}