import subprocess
import json

full_cwa_text = """ 
(a) In general
(1) Grants to States
The Administrator may make grants to States for the purpose of providing grants to a municipality or municipal entity for planning, design, and construction of—

(A) treatment works to intercept, transport, control, treat, or reuse municipal combined sewer overflows, sanitary sewer overflows, or stormwater;

(B) notification systems to inform the public of combined sewer or sanitary overflows that result in sewage being released into rivers and other waters; and

(C) any other measures to manage, reduce, treat, or recapture stormwater or subsurface drainage water eligible for assistance under section 1383(c) of this title.

(2) Direct municipal grants
Subject to subsection (g), the Administrator may make a direct grant to a municipality or municipal entity for the purposes described in paragraph (1).

(b) Prioritization
In selecting from among municipalities applying for grants under subsection (a), a State or the Administrator shall give priority to an applicant that—

(1) is a municipality that is a financially distressed community under subsection (c);

(2) has implemented or is complying with an implementation schedule for the nine minimum controls specified in the CSO control policy referred to in section 1342(q)(1) of this title and has begun implementing a long-term municipal combined sewer overflow control plan or a separate sanitary sewer overflow control plan;

(3) is requesting a grant for a project that is on a State's intended use plan pursuant to section 1386(c) of this title; or

(4) is an Alaska Native Village.

(c) Financially distressed community
(1) Definition
In subsection (b), the term "financially distressed community" means a community that meets affordability criteria established by the State in which the community is located, if such criteria are developed after public review and comment.

(2) Consideration of impact on water and sewer rates
In determining if a community is a distressed community for the purposes of subsection (b), the State shall consider, among other factors, the extent to which the rate of growth of a community's tax base has been historically slow such that implementing a plan described in subsection (b)(2) would result in a significant increase in any water or sewer rate charged by the community's publicly owned wastewater treatment facility.

(3) Information to assist States
The Administrator may publish information to assist States in establishing affordability criteria under paragraph (1).

(d) Cost-sharing
(1) In general
The Federal share of the cost of activities carried out using amounts from a grant made under subsection (a) shall be not less than 55 percent of the cost.

(2) Rural and financially distressed communities
To the maximum extent practicable, the Administrator shall work with States to prevent the non-Federal share requirements under this subsection from being passed on to rural communities and financially distressed communities (as those terms are defined in subsection (f)(2)(B)(i)).

(3) Types of non-Federal share
The applicable non-Federal share of the cost under this subsection may include, in any amount, public and private funds and in-kind services, and may include, notwithstanding section 1383(h) of this title, financial assistance, including loans, from a State water pollution control revolving fund.

(e) Administrative requirements
A project that receives assistance under this section shall be carried out subject to the same requirements as a project that receives assistance from a State water pollution control revolving fund under subchapter VI of this chapter, except to the extent that the Governor of the State in which the project is located determines that a requirement of subchapter VI of this chapter is inconsistent with the purposes of this section. For the purposes of this subsection, a Governor may not determine that the requirements of subchapter VI of this chapter relating to the application of section 1372 of this title are inconsistent with the purposes of this section.

(f) Authorization of appropriations
(1) In general
There is authorized to be appropriated to carry out this section $280,000,000 for each of fiscal years 2022 through 2026.

(2) Minimum allocations
(A) Green projects
To the extent there are sufficient eligible project applications, the Administrator shall ensure that a State uses not less than 20 percent of the amount of the grants made to the State under subsection (a) in a fiscal year to carry out projects to intercept, transport, control, treat, or reuse municipal combined sewer overflows, sanitary sewer overflows, or stormwater through the use of green infrastructure, water and energy efficiency improvements, and other environmentally innovative activities.

(B) Rural or financially distressed community allocation
(i) Definitions
In this subparagraph:

(I) Financially distressed community
The term "financially distressed community" has the meaning given the term in subsection (c)(1).

(II) Rural community
The term "rural community" means a city, town, or unincorporated area that has a population of not more than 10,000 inhabitants.

(ii) Allocation
(I) In general
To the extent there are sufficient eligible project applications, the Administrator shall ensure that a State uses not less than 25 percent of the amount of the grants made to the State under subsection (a) in a fiscal year to carry out projects in rural communities or financially distressed communities for the purpose of planning, design, and construction of—

(aa) treatment works to intercept, transport, control, treat, or reuse municipal sewer overflows, sanitary sewer overflows, or stormwater; or

(bb) any other measures to manage, reduce, treat, or recapture stormwater or subsurface drainage water eligible for assistance under section 603(c).

(II) Rural communities
Of the funds allocated under subclause (I) for the purposes described in that subclause, to the extent there are sufficient eligible project applications, the Administrator shall ensure that a State uses not less than 60 percent to carry out projects in rural communities.

(g) Allocation of funds
(1) Fiscal year 2019
Subject to subsection (h), the Administrator shall use the amounts appropriated to carry out this section for fiscal year 2019 for making grants to municipalities and municipal entities under subsection (a)(2) in accordance with the criteria set forth in subsection (b).

(2) Fiscal year 2020 and thereafter
Subject to subsection (h), the Administrator shall use the amounts appropriated to carry out this section for fiscal year 2020 and each fiscal year thereafter for making grants to States under subsection (a)(1) in accordance with a formula to be established by the Administrator, after providing notice and an opportunity for public comment, that allocates to each State a proportional share of such amounts based on the total needs of the State for municipal combined sewer overflow controls, sanitary sewer overflow controls, and stormwater identified in the most recent detailed estimate and comprehensive study submitted pursuant to section 1375 of this title and any other information the Administrator considers appropriate.

(h) Administrative expenses
Of the amounts appropriated to carry out this section for each fiscal year—

(1) the Administrator may retain an amount not to exceed 1 percent for the reasonable and necessary costs of administering this section; and

(2) the Administrator, or a State, may retain an amount not to exceed 4 percent of any grant made to a municipality or municipal entity under subsection (a), for the reasonable and necessary costs of administering the grant.

(i) Reports
(1) Periodic reports
(A) In general
Not later than December 31, 2003, and periodically thereafter, the Administrator shall transmit to Congress a report containing—

(i) recommended funding levels for grants under this section; and

(ii) a description of the extent to which States pass costs associated with the non-Federal share requirements under subsection (d) to local communities, with a focus on rural communities and financially distressed communities (as those terms are defined in subsection (f)(2)(B)(i)).

(B) Requirement
The funding levels recommended under subparagraph (A)(i) shall be sufficient to ensure the continued expeditious implementation of municipal combined sewer overflow and sanitary sewer overflow controls nationwide.

(2) Use of funds
Not later than 2 years after November 15, 2021, the Administrator shall submit to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report that describes the implementation of the grant program under this section, which shall include a description of the grant recipients, sources of funds for non-Federal share requirements under subsection (d), and grant amounts made available under the program.
"""

escaped_json_string = json.dumps(full_cwa_text, ensure_ascii=False)

subprocess.run("pbcopy", text=True, input=escaped_json_string, check=True)

print("Escaped JSON string copied to clipboard! ")