# Generated by Django 2.2.6 on 2021-03-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='BackendTaskRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField(default=0, verbose_name='业务ID')),
                ('task_id', models.CharField(db_index=True, max_length=256, verbose_name='task_id')),
                ('task_type', models.CharField(default='', max_length=256, verbose_name='task_type')),
                ('task_step', models.TextField(default='', verbose_name='task_step')),
                ('task_result', models.TextField(default='', verbose_name='task_result')),
                (
                    'task_status',
                    models.IntegerField(
                        choices=[
                            (1, '未执行'),
                            (2, '正在执行'),
                            (3, '行完成且成功'),
                            (4, '执行失败'),
                            (5, '跳过'),
                            (6, '忽略错误'),
                            (7, '等待用户'),
                            (8, '手动结束'),
                            (9, '状态异常'),
                            (10, '步骤强制终止中'),
                            (11, '步骤强制终止成功'),
                            (12, '步骤强制终止失败'),
                        ],
                        default=0,
                        verbose_name='结果表任务状态',
                    ),
                ),
                ('child_task_info', models.TextField(default='[]', verbose_name='子任务信息')),
                ('alert_status', models.IntegerField(choices=[(0, '未告警'), (1, '已告警')], default=0, verbose_name='告警状态')),
                ('is_delete', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='删除标志')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={'verbose_name': '后台任务记录表', 'verbose_name_plural': '后台任务记录表',},
        ),
        migrations.CreateModel(
            name='EsCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_name', models.CharField(default='', max_length=100, unique=True, verbose_name='集群名称')),
                ('app', models.CharField(default='', max_length=100, verbose_name='业务')),
                ('appid', models.CharField(default='', max_length=100, verbose_name='业务id')),
                ('yun', models.CharField(default='', max_length=50, verbose_name='云环境')),
                ('zone', models.CharField(default='', max_length=100, verbose_name='地区')),
                ('master_list', models.CharField(default='', max_length=100, verbose_name='master列表')),
                ('masters', models.CharField(default='', max_length=100, verbose_name='master数量')),
                ('datas', models.CharField(default='', max_length=100, verbose_name='数据节点数量')),
                ('colds', models.CharField(default='', max_length=100, verbose_name='冷节点数量')),
                ('clients', models.CharField(default='', max_length=100, verbose_name='协调节点数量')),
                ('version', models.CharField(default='', max_length=100, verbose_name='版本号')),
                ('http_port', models.CharField(default='6300', max_length=100, verbose_name='http端口号')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('address', models.CharField(default='', max_length=100, verbose_name='版本号')),
                ('description', models.CharField(default='', max_length=100, verbose_name='集群描述')),
                ('created_by', models.CharField(default='system', max_length=256, verbose_name='创建人')),
                ('is_delete', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='删除标志')),
            ],
        ),
        migrations.CreateModel(
            name='EsFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default='', max_length=128, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('struct', models.TextField(default=None)),
                ('status', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='EsNodeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(default='', max_length=50, verbose_name='业务')),
                ('cluster_name', models.CharField(db_index=True, default='', max_length=50, verbose_name='集群名称')),
                ('node_name', models.CharField(db_index=True, default='', max_length=50, verbose_name='节点名称')),
                ('ip', models.CharField(default='', max_length=50, verbose_name='节点ip')),
                ('zone', models.CharField(default='', max_length=50, verbose_name='节点在机房')),
                ('role', models.CharField(default='', max_length=50, verbose_name='节点角色')),
                ('version', models.CharField(default='', max_length=50, verbose_name='es版本')),
                ('device_class', models.CharField(default='', max_length=50, verbose_name='设备类型')),
                ('hard_memo', models.CharField(default='', max_length=50, verbose_name='硬件说明')),
            ],
        ),
        migrations.CreateModel(
            name='EsRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(default='', max_length=100, verbose_name='业务')),
                ('appid', models.CharField(default='', max_length=100, verbose_name='业务id')),
                ('cluster_name', models.CharField(default='', max_length=100, verbose_name='集群名称')),
                ('user_name', models.CharField(default='', max_length=100, verbose_name='用户名称')),
            ],
        ),
        migrations.CreateModel(
            name='EsTaskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(default='', max_length=100, verbose_name='业务ID')),
                ('task_id', models.CharField(db_index=True, max_length=256, verbose_name='task_id')),
                ('task_type', models.CharField(default='', max_length=256, verbose_name='task_type')),
                ('cluster_name', models.CharField(default='', max_length=100, verbose_name='集群名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='创建时间')),
                ('task_status', models.IntegerField(default=0, verbose_name='结果表任务状态')),
                ('created_by', models.CharField(default='system', max_length=100, verbose_name='创建人')),
            ],
        ),
    ]
