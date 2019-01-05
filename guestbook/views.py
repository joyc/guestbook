from flask import flash, redirect, url_for, render_template

from guestbook import app, db
from guestbook.models import Message
from guestbook.forms import GuestbookForm


@app.route('/', methods=["GET", "POST"])
def index():
    # 获取所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = GuestbookForm()
    if form.validate_on_submit():
        name = form.name.data
        content = form.content.data
        # 实例化Message并创建记录
        message = Message(content=content, name=name)
        db.session.add(message)
        db.session.commit()
        flash('留言已提交！')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
