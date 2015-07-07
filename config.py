"""Global configuration of the Flask application"""
from __future__ import print_function
import os
import sys


def usage_warning(message):
    """Terminate application and display message if misconfigured."""
    print(message)
    sys.exit()


class DefaultConfig(object):
    """Configure default settings for all app environments."""

    # Site title
    SITE_TITLE = os.environ.get('SITE_TITLE')  or usage_warning('Site title'
                                                                ' not set.')

    # Site domain anatomy and FQDN assembly
    SITE_PROTOCOL = (os.environ.get('SITE_PROTOCOL') or
                     usage_warning('Site Protocol not set.'))
    SITE_SUBDOMAIN = (os.environ.get('SITE_SUBDOMAIN') or
                      usage_warning('Subdomain not set.'))
    SITE_DOMAIN = (os.environ.get('SITE_DOMAIN') or
                   usage_warning('Site domain not set.'))
    SITE_TLD = os.environ.get('SITE_TLD') or usage_warning('Site TLD not set.')
    SITE_FQDN = '{0}.{1}.{2}'.format(SITE_SUBDOMAIN, SITE_DOMAIN, SITE_TLD)

    # Static file server domain anatomy and FQDN assembly
    STATIC_ASSET_PROTOCOL = (os.environ.get('STATIC_ASSET_PROTOCOL') or
                             usage_warning('Site Protocol not set.'))
    STATIC_ASSET_SUBDOMAIN = (os.environ.get('STATIC_ASSET_SUBDOMAIN') or
                              usage_warning('Subdomain not'))

    STATIC_ASSET_DOMAIN = (os.environ.get('STATIC_ASSET_DOMAIN') or
                           usage_warning('Site domain not set.'))
    STATIC_ASSET_TLD = (os.environ.get('STATIC_ASSET_TLD') or
                        usage_warning('Site TLD not set.'))
    STATIC_ASSET_FQDN = '{0}.{1}.{2}'.format(STATIC_ASSET_SUBDOMAIN,
                                             STATIC_ASSET_DOMAIN,
                                             STATIC_ASSET_TLD)

    # Redirection domain anatomy and FQDN assembly
    REDIRECTION_PROTOCOL = (os.environ.get('REDIRECTION_PROTOCOL') or
                            usage_warning('Site Protocol not set.'))
    REDIRECTION_SUBDOMAIN = (os.environ.get('REDIRECTION_SUBDOMAIN') or
                             usage_warning('Subdomain not set.'))
    REDIRECTION_DOMAIN = (os.environ.get('REDIRECTION_DOMAIN') or
                          usage_warning('Site domain not set.'))
    REDIRECTION_TLD = (os.environ.get('REDIRECTION_TLD') or
                       usage_warning('Site TLD not set.'))
    REDIRECTION_FQDN = '{0}.{1}.{2}'.format(REDIRECTION_SUBDOMAIN,
                                            REDIRECTION_DOMAIN,
                                            REDIRECTION_TLD)

    # Default "FROM" E-mail address
    ADMIN_EMAIL_SENDER = '{0} <noreply@{1}.{2}>'.format(SITE_TITLE,
                                                        SITE_DOMAIN,
                                                        SITE_TLD)

    # Used for hashing and encryption
    SECRET_KEY = (os.environ.get('SECRET_KEY') or
                  usage_warning('SECRET_KEY not configured.'))

    # Ensures that DB interactions are committed
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Called from create_app() after specific configuration is selected
    @staticmethod
    def init_app(app):
        """Leave me here. Essential to bootstrap."""
        pass


class DevelopmentConfig(DefaultConfig):
    """Configure dev environment."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               usage_warning('DEV database URL not '
                                             'configured.'))


class TestingConfig(DefaultConfig):
    """Configure testing environment."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('TEST_DATABASE_URL') or
                               usage_warning('TEST database URL not'
                                             ' configured.'))


class StagingConfig(DefaultConfig):
    """Configure staging environment."""
    STAGING = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('STAGE_DATABASE_URL') or
                               usage_warning('STAGE database URL not '
                                             'configured.'))

class ProductionConfig(DefaultConfig):
    """Configure production environment."""
    PRODUCTION = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('PROD_DATABASE_URL') or
                               usage_warning('PROD database URL not'
                                             'configured.'))

CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
