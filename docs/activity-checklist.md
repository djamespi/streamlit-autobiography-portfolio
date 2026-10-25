# Activity coverage

Source: the supplied two-page Streamlit Autobiography and Portfolio activity. The lesson deck provides examples of Streamlit text, charts, widgets, layout, caching, and session state. Its example OpenAI chatbot does not require this portfolio to call OpenAI.

| Activity requirement | Implementation | Content status |
| --- | --- | --- |
| Name, program/year, short biography, visible section | Header, sidebar, footer | Supplied by Dexter |
| Photo or labeled stand-in | `assets/portrait-stand-in.svg` | Implemented |
| Background, education, interests, milestones in own words | Story tabs | Paraphrased from Dexter's supplied autobiography |
| Skills in text and a table/chart using own numbers | Rating scale, chart, table, evidence | Dexter's ratings: backend 4, QA 3, AI 3 |
| Three projects, role, tools, outcome or link | Searchable project cards | TeknoCare, Habitually, CS345 backpropagation; verified public source and contributor metadata |
| Contact or feedback form with response | Validated form and session receipt | Implemented |
| Text, table, chart | Headings, Markdown, dataframe, Altair chart | Implemented with Dexter's ratings |
| Button, slider, selectbox, checkbox | Reset, skill threshold, ordering, table toggle | Implemented |
| Text input, text area, radio/multiselect | Search, form, navigation, tools filter | Implemented |
| Sidebar and columns | Navigation and section layouts | Implemented |
| Four or more extras | Image, tabs, metrics, form, session state, download, theme, expanders | Implemented |
| Public Community Cloud link for Option B | Public GitHub repo `djamespi/streamlit-autobiography-portfolio`, branch `main`, entrypoint `app.py` | Dexter will deploy through Community Cloud and submit the resulting public link |

The source activity says the writing and projects must be the student's own. Autobiographical facts and ratings come from Dexter. Project entries describe his public repositories; roles reflect ownership and contribution metadata, with supplied coursework code distinguished from modifications. `check_content.py` reports content gaps before submission.
