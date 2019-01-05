import click
from guestbook import app, db
from guestbook.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='此操作会先删除后创建DB')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('此操作会删除现有DB，是否继续?', abort=True)
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库成功')


@app.cli.command()
@click.option('--count', default=20, help='数据条数，默认20条')
def forge(count):
    """生成测试数据"""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker('zh_CN')
    click.echo('生成中...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            content=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo(f'创建了{count}条数据')
