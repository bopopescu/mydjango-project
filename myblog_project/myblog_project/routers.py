class DBRouter(object):
    """
    Docs:hrrps://docs.djangoproject.com/en/1.9/topics/db/multi-db/#an-example
    A router to control all database operations on models in the auth application.
    $ ./manage.py migrate
    $ ./manage.py migrate --database=geo
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to 'geo'.
        """
        if model._meta.app_label == 'auth':
            return 'geo'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attenps to write auth models go to 'geo'.
        """
        if model._meta.app_label == 'auth':
            return 'geo'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is invoved.
        """
        if obj1._meta.app_label == 'auth' or obj2._meta.app_label == 'auth':
            return True
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db' database.
        :param db:
        :param app_label:
        :param model_name:
        :param hints:
        :return:
        """

        if app_label == 'auth':
            return db == 'geo'
        return 'default'