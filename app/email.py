"""Send async e-mail easily from within app."""
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):
    """Send e-mail asynchronously."""
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    """Compose e-mail message and pass to send_async_email"""
    app = current_app._get_current_object() # pylint: disable=W0212
    msg = Message(subject, sender=app.config['ADMIN_EMAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
