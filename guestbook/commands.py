import click
from guestbook import app, db


@app.cli.command()
@click.option('--drop', is_flag=True, help='此操作会先删除后创建DB')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('此操作会删除现有DB，是否继续?', abort=True)
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库成功')

