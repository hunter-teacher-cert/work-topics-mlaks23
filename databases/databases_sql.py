
#This SQL JOIN query will retrieve the records of all of the unexcused period attendance absences in the school for the week of 1-24-22 sorted by student last name ascending.


SELECT First, Last, StudentID, Grade, ScanTime, Status, CourseSection, Attendance, Period, Teacher
FROM (
  SELECT scan.First, scan.Last, scan.StudentID, scan.Grade, ScanTime, Status, CourseSection, Attendance, Period, Teacher
  FROM scan
  LEFT JOIN periodAtt AS period
  ON scan.StudentID=period.StudentID AND SUBSTR(scan.ScanTime, 1, 9)=period.Date
  WHERE Attendance="A"
  ORDER BY scan.LAST)
AS allCuts



# Link to google collab:
# https://colab.research.google.com/drive/1ZPpocGnjOFJyIL39Rwr29cqaogOLdNnr#scrollTo=6XydmJWGYia4
