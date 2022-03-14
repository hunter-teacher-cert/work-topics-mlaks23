SELECT First, Last, studentID, Grade, Scantime, (Period=1) AS pd1, Date, CourseSection
FROM
(
SELECT t1.First, t1.Last, t1.studentID, t1.Grade, t1.ScanTime, t1.Status, Date, CourseSection, Attendance, Teacher, Period
FROM scan AS t1
INNER JOIN periodAtt AS t2
ON t1.studentID=t2.studentID AND SUBSTR(t1.scanTime, 1, 9)=t2.date
WHERE Attendance="A"
ORDER BY t1.Last ASC)
AS allCuts
