---
created: <% tp.file.creation_date() %>
tag: daily_note
---
# <% tp.date.now("dddd, MMMM DD, YYYY") %>
---
<< [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD').subtract(1, 'd').format('YYYY-MM-DD') %>|Yesterday]] | [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD').add(1, 'd').format('YYYY-MM-DD') %>|Tomorrow]] >>

----
<% tp.web.daily_quote() %>


### This day last year

![[<% tp.date.now("YYYY-MM-DD", "P-1Y") %>]]

## Open Tasks
```dataview
TASK 
WHERE status = " " 
```
## Notes




---

## Contact

*Who did I talk to today?*

  

## To Explore Later

---

## Evening Reflection

  

## What did I learn today?


---
### Documents Created Today
```dataview
list
WHERE date(datecreated).month = this.file.day.month
```
### Notes last touched today
```dataview
List
WHERE file.mday = this.file.day.month
SORT file.mtime asc
```