# Generated by Django 4.1.3 on 2022-12-06 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('assessmentid', models.AutoField(db_column='AssessmentID', primary_key=True, serialize=False)),
                ('assessmentname', models.CharField(blank=True, db_column='AssessmentName', max_length=45, null=True)),
                ('totalmarks', models.IntegerField(blank=True, db_column='TotalMarks', null=True)),
            ],
            options={
                'db_table': 'assessment',
            },
        ),
        migrations.CreateModel(
            name='Clo',
            fields=[
                ('cloid', models.AutoField(db_column='CLOID', primary_key=True, serialize=False)),
                ('clonum', models.CharField(db_column='CLONum', max_length=45)),
                ('clodescription', models.CharField(db_column='CLODescription', max_length=2000)),
                ('bloomc', models.CharField(blank=True, db_column='BloomC', max_length=45, null=True)),
                ('bloomp', models.CharField(blank=True, db_column='BloomP', max_length=45, null=True)),
                ('blooma', models.CharField(blank=True, db_column='BloomA', max_length=45, null=True)),
                ('copocorrelation', models.CharField(blank=True, db_column='COPOCorrelation', max_length=45, null=True)),
            ],
            options={
                'db_table': 'clo',
            },
        ),
        migrations.CreateModel(
            name='CourseOutline',
            fields=[
                ('coid', models.AutoField(db_column='CoID', primary_key=True, serialize=False)),
                ('deptname', models.CharField(blank=True, db_column='DeptName', max_length=80, null=True)),
                ('schoolname', models.CharField(blank=True, db_column='SchoolName', max_length=400, null=True)),
                ('coursecode', models.CharField(blank=True, db_column='CourseCode', max_length=45, null=True)),
                ('coursetitle', models.CharField(blank=True, db_column='CourseTitle', max_length=45, null=True)),
                ('coursetype', models.CharField(blank=True, db_column='CourseType', max_length=45, null=True)),
                ('courseprereq', models.CharField(blank=True, db_column='CoursePrerequisite', max_length=45, null=True)),
                ('creditvalue', models.CharField(blank=True, db_column='CreditValue', max_length=45, null=True)),
                ('contacthour_week', models.CharField(blank=True, db_column='ContactHour/Week', max_length=45, null=True)),
                ('coursedescription', models.CharField(blank=True, db_column='CourseDescription', max_length=3000, null=True)),
                ('courseobjective', models.CharField(blank=True, db_column='CourseObjective', max_length=3000, null=True)),
                ('coursecontent', models.CharField(blank=True, db_column='CourseContent', max_length=3000, null=True)),
                ('assessmenttype', models.CharField(blank=True, db_column='AssessmentType', max_length=45, null=True)),
                ('referencebook', models.CharField(blank=True, db_column='ReferenceBook', max_length=3000, null=True)),
            ],
            options={
                'db_table': 'course_outline',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('departmentid', models.AutoField(db_column='DepartmentID', primary_key=True, serialize=False)),
                ('departmentname', models.CharField(blank=True, db_column='DepartmentName', max_length=65, null=True)),
                ('departmentdetails', models.CharField(blank=True, db_column='DepartmentDetails', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeid', models.IntegerField(db_column='EmployeeID', primary_key=True, serialize=False)),
                ('employeename', models.CharField(blank=True, db_column='EmployeeName', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=45, null=True)),
                ('employeetype', models.CharField(blank=True, db_column='EmployeeType', max_length=45, null=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('programid', models.AutoField(db_column='ProgramID', primary_key=True, serialize=False)),
                ('programname', models.CharField(blank=True, db_column='ProgramName', max_length=100, null=True)),
                ('programdetail', models.CharField(blank=True, db_column='ProgramDetail', max_length=1000, null=True)),
                ('departmentid', models.ForeignKey(blank=True, db_column='DepartmentID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.department')),
            ],
            options={
                'db_table': 'program',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('schoolid', models.AutoField(db_column='SchoolID', primary_key=True, serialize=False)),
                ('schoolname', models.CharField(blank=True, db_column='SchoolName', max_length=45, null=True)),
                ('schooldetails', models.CharField(blank=True, db_column='SchoolDetails', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'school',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('sectionid', models.AutoField(db_column='SectionID', primary_key=True, serialize=False)),
                ('courseid', models.IntegerField(blank=True, db_column='CourseID', null=True)),
                ('sectionnum', models.CharField(blank=True, db_column='SectionNum', max_length=45, null=True)),
                ('semester', models.CharField(blank=True, db_column='Semester', max_length=45, null=True)),
                ('year', models.TextField(blank=True, db_column='Year', null=True)),
            ],
            options={
                'db_table': 'section',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('femployeeid', models.OneToOneField(db_column='FEmployeeID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='CMAS.employee')),
            ],
            options={
                'db_table': 'faculty',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentid', models.CharField(db_column='StudentID', max_length=50, primary_key=True, serialize=False)),
                ('studentname', models.CharField(blank=True, db_column='StudentName', max_length=75, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=75, null=True)),
                ('programid', models.ForeignKey(blank=True, db_column='ProgramID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.program')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionid', models.AutoField(db_column='QuestionID', primary_key=True, serialize=False)),
                ('questionnumber', models.CharField(blank=True, db_column='QuestionNumber', max_length=45, null=True)),
                ('questiondetail', models.CharField(blank=True, db_column='QuestionDetail', max_length=3000, null=True)),
                ('marks', models.IntegerField(blank=True, db_column='Marks', null=True)),
                ('assessmentid', models.ForeignKey(blank=True, db_column='AssessmentID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.assessment')),
                ('cloid', models.ForeignKey(blank=True, db_column='CLOID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.clo')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Plo',
            fields=[
                ('ploid', models.AutoField(db_column='PLOID', primary_key=True, serialize=False)),
                ('plonum', models.CharField(blank=True, db_column='PLONum', max_length=45, null=True)),
                ('plodetail', models.CharField(blank=True, db_column='PLODetail', max_length=2000, null=True)),
                ('programid', models.ForeignKey(blank=True, db_column='ProgramID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.program')),
            ],
            options={
                'db_table': 'plo',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='schoolid',
            field=models.ForeignKey(blank=True, db_column='SchoolID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.school'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.AutoField(db_column='CourseID', primary_key=True, serialize=False)),
                ('coursename', models.CharField(blank=True, db_column='CourseName', max_length=100, null=True)),
                ('coursedescription', models.CharField(blank=True, db_column='CourseDescription', max_length=2000, null=True)),
                ('coursedetail', models.CharField(blank=True, db_column='CourseDetail', max_length=200, null=True)),
                ('programid', models.ForeignKey(blank=True, db_column='ProgramID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.program')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.AddField(
            model_name='clo',
            name='courseid',
            field=models.ForeignKey(db_column='CourseID', on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.course'),
        ),
        migrations.AddField(
            model_name='clo',
            name='ploid',
            field=models.ForeignKey(db_column='PLOID', on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.plo'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='sectionid',
            field=models.ForeignKey(blank=True, db_column='SectionID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.section'),
        ),
        migrations.AddField(
            model_name='section',
            name='femployeeid',
            field=models.ForeignKey(blank=True, db_column='FEmployeeID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.faculty'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='departmentid',
            field=models.ForeignKey(blank=True, db_column='DepartmentID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.department'),
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('studentid', models.IntegerField(db_column='StudentID', primary_key=True, serialize=False)),
                ('obtainedmarks', models.IntegerField(blank=True, db_column='ObtainedMarks', null=True)),
                ('questionid', models.ForeignKey(db_column='QuestionID', on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.question')),
            ],
            options={
                'db_table': 'evaluation',
                'unique_together': {('studentid', 'questionid')},
            },
        ),
        migrations.CreateModel(
            name='DepartmentHead',
            fields=[
                ('dhemployeeid', models.OneToOneField(db_column='DHEmployeeID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='CMAS.employee')),
                ('departmentid', models.ForeignKey(blank=True, db_column='DepartmentID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.department')),
            ],
            options={
                'db_table': 'department_head',
            },
        ),
        migrations.CreateModel(
            name='Dean',
            fields=[
                ('demployeeid', models.OneToOneField(db_column='DemployeeID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='CMAS.employee')),
                ('schoolid', models.ForeignKey(blank=True, db_column='SchoolID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.school')),
            ],
            options={
                'db_table': 'dean',
            },
        ),
        migrations.CreateModel(
            name='CourseLesson',
            fields=[
                ('coid', models.OneToOneField(db_column='CoID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='CMAS.courseoutline')),
                ('week', models.CharField(db_column='Week', max_length=45)),
                ('topic', models.CharField(blank=True, db_column='Topic', max_length=45, null=True)),
                ('teachingstrategy', models.CharField(blank=True, db_column='TeachingStrategy', max_length=1000, null=True)),
                ('assessmentstrategy', models.CharField(blank=True, db_column='AssessmentStrategy', max_length=1000, null=True)),
                ('clolevel', models.CharField(blank=True, db_column='CLOLevel', max_length=45, null=True)),
            ],
            options={
                'db_table': 'course_lesson',
                'unique_together': {('coid', 'week')},
            },
        ),
        migrations.CreateModel(
            name='CourseEvaluation',
            fields=[
                ('coid', models.OneToOneField(db_column='CoID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='CMAS.courseoutline')),
                ('assessmenttools', models.CharField(db_column='AssessmentTools', max_length=45)),
                ('marksdistribution', models.CharField(blank=True, db_column='MarksDistribution', max_length=45, null=True)),
                ('bloomcategory', models.CharField(blank=True, db_column='BloomCategory', max_length=100, null=True)),
            ],
            options={
                'db_table': 'course_evaluation',
                'unique_together': {('coid', 'assessmenttools')},
            },
        ),
    ]
