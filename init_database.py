import pymysql
import models.secret as secret
from utils import log


def add_guest():
    cmd = 'INSERT INTO User VALUES (-1, \'【游客】\',\'NULL\',\'guest\')'
    return cmd


def create_user():
    cmd = 'CREATE TABLE IF NOT EXISTS `User`(' \
          '`id` INT AUTO_INCREMENT,' \
          '`username` VARCHAR(32) NOT NULL,' \
          '`password` VARCHAR(64) NOT NULL,' \
          '`role` VARCHAR(10) NOT NULL DEFAULT \'normal\',' \
          'PRIMARY KEY (`id`)' \
          ');'
    return cmd


def creat_session():
    cmd = 'CREATE TABLE IF NOT EXISTS `Session`(' \
          '`id` INT AUTO_INCREMENT,' \
          '`session_id` VARCHAR(36) NOT NULL,' \
          '`user_id` INT NOT NULL,' \
          '`expired_time` INT NOT NULL,' \
          'PRIMARY KEY (`id`)' \
          ');'
    return cmd


def creat_weibo():
    cmd = 'CREATE TABLE IF NOT EXISTS `Weibo`(' \
          '`id` INT AUTO_INCREMENT,' \
          '`content` TEXT NOT NULL,' \
          '`user_id` INT NOT NULL,' \
          '`writer` VARCHAR(32) NOT NULL,' \
          '`update_time` VARCHAR(32) NOT NULL,' \
          '`create_time` VARCHAR(32) NOT NULL,' \
          'PRIMARY KEY (`id`)' \
          ');'
    return cmd


def creat_comment():
    cmd = 'CREATE TABLE IF NOT EXISTS `Comment`(' \
          '`id` INT AUTO_INCREMENT,' \
          '`content` TEXT NOT NULL,' \
          '`user_id` INT NOT NULL,' \
          '`weibo_id` INT NOT NULL,' \
          '`writer` VARCHAR(32) NOT NULL,' \
          '`update_time` VARCHAR(32) NOT NULL,' \
          '`create_time` VARCHAR(32) NOT NULL,' \
          'PRIMARY KEY (`id`)' \
          ');'
    return cmd


def init_database(db_name, db_pass):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=db_pass,
        db=db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    user = create_user()
    session = creat_session()
    weibo = creat_weibo()
    comment = creat_comment()
    guest = add_guest()
    with connection.cursor() as cursor:
        cursor.execute(user)
        cursor.execute(session)
        cursor.execute(weibo)
        cursor.execute(comment)
        cursor.execute(guest)
    connection.commit()


if __name__ == '__main__':
    log('开始创建数据表')
    init_database(secret.db_name, secret.db_pass)
    log('创建完成!')
