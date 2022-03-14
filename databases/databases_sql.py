SELECT First, Last, StudentID, Grade, ScanTime, Status, CourseSection, Attendance, Period, Teacher
FROM (
  SELECT scan.First, scan.Last, scan.StudentID, scan.Grade, ScanTime, Status, CourseSection, Attendance, Period, Teacher
  FROM scan
  LEFT JOIN periodAtt AS period
  ON scan.StudentID=period.StudentID AND SUBSTR(scan.ScanTime, 1, 9)=period.Date
  WHERE Attendance="A"
  ORDER BY scan.LAST)
AS allCuts
