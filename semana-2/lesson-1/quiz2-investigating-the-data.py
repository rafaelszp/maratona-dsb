import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def counts(lines,pk):
    keys = set([e[pk] for e in lines])
    return len(lines),len(keys)


enrollments = read_csv('./enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

enrollment_num_rows,enrollment_num_unique_students = counts(enrollments,'account_key')
engagement_num_rows,engagement_num_unique_students = counts(daily_engagement,'acct')
submission_num_rows,submission_num_unique_students = counts(project_submissions,'account_key')

print enrollment_num_rows,enrollment_num_unique_students
print engagement_num_rows,engagement_num_unique_students
print submission_num_rows,submission_num_unique_students