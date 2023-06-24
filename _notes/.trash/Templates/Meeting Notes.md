---
date: <% tp.file.creation_date() %>
type: meeting
project: {{ask:"Enter the project name (leave empty for general meeting)"}}
---
tags: [[#meetings]]
Date: [[<% tp.date.now("YYYY-MM-DD-dddd") %>]]
<% await tp.file.move("Meetings/" + tp.date.now("YYYY-MM-DD") + " " + tp.file.title) %>
# [[<% tp.date.now("YYYY-MM-DD") + " " + tp.file.title %>]]

# Meeting Details
- **Topic:** <% tp.file.title %>  
- **Location:** <% tp.system.suggester(["Virtual", "In Person"], ["Virtual", "In Person"]) %>
- **Date:** <% tp.file.title.split(" ")[0] %>
- **Time/Duration:** xx:xx - xx:xx
- **Attendees**: 
	- 
---
# Agenda

# Action Items/Questions
- 

## Notes

## Resources