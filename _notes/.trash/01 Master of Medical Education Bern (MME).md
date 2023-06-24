## Programminformation
Das Master of Medical Education Programm Bern (MME Bern) ist ein berufsbegleitender medizindidaktischer Weiterbildungsstudiengang der Medizinischen Fakultät der Universität Bern. Der Studiengang wurde in Zusammenarbeit mit der University of Illinois in Chicago entwickelt und ist seit 1999 etabliert.

Das Programm basiert auf einem systematischen, evidenz-basierten Ansatz und bereitet die Teilnehmenden so auf die wachsenden Herausforderungen in Aus- und Weiterbildung im Gesundheitswesen vor.

Der Studiengang engagiert internationale Experten und wird für Absolventen aller Gesundheits­berufe angeboten. Das Programm erfordert die Präsenz der Teilnehmenden in den während zwei Jahren angebotenen Kurswochen.

## Die Ziele des MME Programms

Das seit 1999 etablierte MME- Programm Bern bietet den Teilnehmern ein breites [Kursangebot](https://www.iml.unibe.ch/angebote/lehre/master-of-medical-education-mme/studieninhalte#headline_695 "Kursangebot") mit folgenden Zielen

- Entwicklung medizindidaktisch kompetenter Führungspersonen
- Vermittlung von Kenntnissen evidenz-basierter Lehr und Unterrichtsmethoden
- Unterstützung bei der Entwicklung innovativer Lehrprojekte und Curricula
- Förderung von Führungsqualitäten im medizinischen Umfeld
- Vermittlung wissenschaftlicher Kenntnisse in der medizindidaktischen Forschung
- Vernetzung mit internationalen und nationalen Experten
- Aufbau eine Netzwerks unter den Teilnehmern und Schaffung einer aktiven, kollaborativen Lernumgebung

# Target audience

**The MME programme is targeted at interested persons in Switzerland and abroad, who have completed a university degree in human medicine, dentistry, veterinary medicine or pharmacy, who carry out teaching activity and hold a leadership function at a medical faculty, or hold equivalent employment in the healthcare sector.**

Admission is also possible for qualified persons from other professions in the healthcare sector (university, university of applied sciences or equivalent at tertiary education level II). In such cases, please contact the programme director in advance.

Over 90% of the course is conducted in English. In some modules like module 2 on communication, German is also spoken. A good knowledge of English is a prerequisite for participation in the course. The programme can still be attended if a participant lacks knowledge of German.

# Contents
**1. Module 1 - Setting the Stage for Medical Education**
	1. Identifying Medical Education Challenges
	2. Fundamentals of Learning and Condition #Skills/Learning/Psychology_of_Learning
	4. Leading Education Change #Skills/Leading
**2. Module 2 - Communication**
	1. Shaping of a Lesson #Skills/Teaching/Lesson_Design
	2. Group Dynamics / Conflict Management #Skills/Project_Management/Group_Management
	4. Professional Communication #Skills/Professional_Communication
**3. Module 3 - Project Management and Curriculum Develpment**
	1. Project Management #Skills/Project_Management
	2. Aims and Goals - Planning Strategies - Curriculum Models - Curriculum Implementation #Skills/Project_Management/Planning #Skills/Teaching/Curriculum_Design
	4. Case-based Supervision #Skills/Case_Supervision
**4. Module 4 - Learning Environment** #Skills/Teaching
	1. Microteaching #Skills/Teaching #Skills/Teaching/Microteaching
	2. Blended Learning #Skills/Teaching/Blended_Learning
	3. Clinical Education 
	4. Group Process #Skills/Teaching/Groups
**5. Module 5 - Assessment** [[Skills Evaluation|#Skills/Evaluation]]
	1. Assessment in the Health Professions
		1. MCQ tests [[Skills Evaluation|#Skills/Evaluation]]/MCQ
		2. OSCE exams and Simulated Patients [[Skills Evaluation|#Skills/Evaluation]]/OSCE [[Skills Evaluation|#Skills/Evaluation]]/Simulated_Patients
		3. Workplace-based Assessment #Skills/Evaluation/Workplace_Assessment
	2. Case-based Supervision #Skills/Case_Supervision
**6. Module 6 - Quantitative Educational Research** #Skills/Research
	1. Organisation of Master Theses Projects #Skills/Research/Master_Thesis #Skills/Research/Supervision
	2. Quantitative Research Design and Methodologies in Education Research #Skills/Research/Quantitative_Research
	3. Reflections on course Program #Teaching_Methods/Feedback
**7. Module 7 - Scholarship/ Qualitative Research I** #Skills/Scholarship
	1. Scholarship in Medical Education
	2. Qualitative Research  #Skills/Research/Qualitative_Research
	3. Case-based Supervision #Skills/Case_Supervision
**8. Module 8 - Qualitative Research II/ Thesis Workshop**
	1. Qualitative Research #Skills/Research/Qualitative_Research
	2. Thesis Workshop  #Skills/Research/Master_Thesis 
	3. Group Process
**9. Module 9 - Leading Educational Change**  #Skills/Leading #Skills/Leading/Change
	1. Faculty Development #Skills/Leading/Faculty
	2. Change Management #Skills/Leading/Management
	3. Case-based Supervision  #Skills/Case_Supervision
**10. Module 10 - Visit of Two Medical Schools Abroad**
	1. on-site abroad visit of Medical Schools
**11. Module 11 - Program Evaluation and Quality Management** #Skills/Project_Management
	1. Program Evaluation and Quality Management  #Skills/Project_Management/QA
	2. Conflict Management #Skills/Project_Management/Conflict
	3. Thesis and Project Coaching #Skills/Leading/Coaching
	4. Case-based Supevision #Skills/Case_Supervision
**12. Module 12 - Special Topics**
	1. Special Topics
	2. Evaluation of MME Program
	3. Master Thesis Presentations
	4. Trends in Medical Educations (DACH)

```dataview
LIST file.tags
FROM "Doctor Thesis/03 Courses/01 Master of Medical Education Bern (MME)"

```

`=this.file.tags`

```dataview
TABLE WITHOUT ID Tag, map(rows, (r) => link(r.file.link, r.title)) AS Notes
FROM "Doctor Thesis/03 Courses/01 Master of Medical Education Bern (MME)"
FLATTEN file.tags as Tag
GROUP BY Tag
WHERE !contains(file.path,this.file.path) AND econtains(this.file.tags, Tag)
```

