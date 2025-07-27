import subprocess
import json

full_cwa_text = """ 

(a) Definitions
In this section:

(1) Coastal Nonpoint Pollution Control Program
The term "Coastal Nonpoint Pollution Control Program" means the State of Washington's Coastal Nonpoint Pollution Control Program approved under section 1455b of title 16.

(2) Director
The term "Director" means the Director of the Program Office.

(3) Federal Action Plan
The term "Federal Action Plan" means the plan developed under subsection (c)(3)(B).

(4) International Joint Commission
The term "International Joint Commission" means the International Joint Commission established by the Treaty relating to the boundary waters and questions arising along the boundary between the United States and Canada, signed at Washington January 11, 1909, and entered into force May 5, 1910 (36 Stat. 2448; TS 548; 12 Bevans 319).

(5) Pacific Salmon Commission
The term "Pacific Salmon Commission" means the Pacific Salmon Commission established by the United States and Canada under the Treaty concerning Pacific salmon, with annexes and memorandum of understanding, signed at Ottawa January 28, 1985, and entered into force March 18, 1985 (TIAS 11091; 1469 UNTS 357) (commonly known as the "Pacific Salmon Treaty").

(6) Program Office
The term "Program Office" means the Puget Sound Recovery National Program Office established by subsection (b).

(7) Puget Sound Action Agenda; Action Agenda
The term "Puget Sound Action Agenda" or"Action Agenda" means the most recent plan developed by the Puget Sound National Estuary Program Management Conference, in consultation with the Puget Sound Tribal Management Conference, and approved by the Administrator as the comprehensive conservation and management plan for the Puget Sound under section 1330 of this title.

(8) Puget Sound Federal Leadership Task Force
The term "Puget Sound Federal Leadership Task Force" means the Puget Sound Federal Leadership Task Force established under subsection (c).

(9) Puget Sound Federal Task Force
The term "Puget Sound Federal Task Force" means the Puget Sound Federal Task Force established in 2016 under a memorandum of understanding among 9 Federal agencies.

(10) Puget Sound National Estuary Program Management Conference
The term "Puget Sound National Estuary Program Management Conference" means the management conference for the Puget Sound convened pursuant to section 1330 of this title.

(11) Puget Sound Partnership
The term "Puget Sound Partnership" means the State agency created under the laws of the State of Washington (section 90.71.210 of the Revised Code of Washington), or its successor agency that has been designated by the Administrator as the lead entity to support the Puget Sound National Estuary Program Management Conference.

(12) Puget Sound region
(A) In general
The term "Puget Sound region" means the land and waters in the northwest corner of the State of Washington from the Canadian border to the north to the Pacific Ocean on the west, including Hood Canal and the Strait of Juan de Fuca.

(B) Inclusion
The term "Puget Sound region" includes all watersheds that drain into the Puget Sound.

(13) Puget Sound Tribal Management Conference
The term "Puget Sound Tribal Management Conference" means the 20 treaty Indian tribes of western Washington and the Northwest Indian Fisheries Commission.

(14) Salish Sea
The term "Salish Sea" means the network of coastal waterways on the west coast of North America that includes the Puget Sound, the Strait of Georgia, and the Strait of Juan de Fuca.

(15) Salmon Recovery Plans
The term "Salmon Recovery Plans" means the recovery plans for salmon and steelhead species approved by the Secretary of the Interior under section 4(f) of the Endangered Species Act of 1973 [16 U.S.C. 1533(f)] that are applicable to the Puget Sound region.

(16) State Advisory Committee
The term "State Advisory Committee" means the advisory committee established by subsection (d).

(17) Treaty Rights at Risk Initiative
The term "Treaty Rights at Risk Initiative" means the report from the treaty Indian tribes of western Washington entitled "Treaty Rights At Risk: Ongoing Habitat Loss, the Decline of the Salmon Resource, and Recommendations for Change" and dated July 14, 2011, or its successor report that outlines issues and offers solutions for the protection of Tribal treaty rights, recovery of salmon habitat, and management of sustainable treaty and nontreaty salmon fisheries, including through Tribal salmon hatchery programs.

(b) Puget Sound Recovery National Program Office
(1) Establishment
There is established in the Environmental Protection Agency a Puget Sound Recovery National Program Office, to be located in the State of Washington.

(2) Director
(A) In general
There shall be a Director of the Program Office, who shall have leadership and project management experience and shall be highly qualified to—

(i) direct the integration of multiple project planning efforts and programs from different agencies and jurisdictions; and

(ii) align numerous, and possibly competing, priorities to accomplish visible and measurable outcomes under the Action Agenda.

(B) Position
The position of Director of the Program Office shall be a career reserved position, as such term is defined in section 3132 of title 5.

(3) Delegation of authority; staffing
Using amounts made available to carry out this section, the Administrator shall delegate to the Director such authority and provide such staff as may be necessary to carry out this section.

(4) Duties
The Director shall—

(A) coordinate and manage the timely execution of the requirements of this section, including the formation and meetings of the Puget Sound Federal Leadership Task Force;

(B) coordinate activities related to the restoration and protection of the Puget Sound across the Environmental Protection Agency;

(C) coordinate and align the activities of the Administrator with the Action Agenda, Salmon Recovery Plans, the Treaty Rights at Risk Initiative, and the Coastal Nonpoint Pollution Control Program;

(D) promote the efficient use of Environmental Protection Agency resources in pursuit of the restoration and protection of the Puget Sound;

(E) serve on the Puget Sound Federal Leadership Task Force and collaborate with, help coordinate, and implement activities with other Federal agencies that have responsibilities involving the restoration and protection of the Puget Sound;

(F) provide or procure such other advice, technical assistance, research, assessments, monitoring, or other support as is determined by the Director to be necessary or prudent to most efficiently and effectively fulfill the objectives and priorities of the Action Agenda, the Salmon Recovery Plans, the Treaty Rights at Risk Initiative, and the Coastal Nonpoint Pollution Control Program, consistent with the best available science, to ensure the health of the Puget Sound ecosystem;

(G) track the progress of the Environmental Protection Agency toward meeting the agency's specified objectives and priorities within the Action Agenda and the Federal Action Plan;

(H) implement the recommendations of the Comptroller General set forth in the report entitled "Puget Sound Restoration: Additional Actions Could Improve Assessments of Progress" and dated July 19, 2018;

(I) serve as liaison and coordinate activities for the restoration and protection of the Salish Sea with Canadian authorities, the Pacific Salmon Commission, and the International Joint Commission; and

(J) carry out such additional duties as the Director determines necessary and appropriate.

(c) Puget Sound Federal Leadership Task Force
(1) Establishment
There is established a Puget Sound Federal Leadership Task Force.

(2) Membership
(A) Composition
The Puget Sound Federal Leadership Task Force shall be composed of the following members:

(i) The following individuals appointed by the Secretary of Agriculture:

(I) A representative of the National Forest Service.

(II) A representative of the Natural Resources Conservation Service.


(ii) A representative of the National Oceanic and Atmospheric Administration appointed by the Secretary of Commerce.

(iii) The following individuals appointed by the Secretary of Defense:

(I) A representative of the Corps of Engineers.

(II) A representative of the Joint Base Lewis-McChord.

(III) A representative of the Commander, Navy Region Northwest.


(iv) The Director of the Program Office.

(v) The following individuals appointed by the Secretary of Homeland Security:

(I) A representative of the Coast Guard.

(II) A representative of the Federal Emergency Management Agency.


(vi) The following individuals appointed by the Secretary of the Interior:

(I) A representative of the Bureau of Indian Affairs.

(II) A representative of the United States Fish and Wildlife Service.

(III) A representative of the United States Geological Survey.

(IV) A representative of the National Park Service.


(vii) The following individuals appointed by the Secretary of Transportation:

(I) A representative of the Federal Highway Administration.

(II) A representative of the Federal Transit Administration.


(viii) Representatives of such other Federal agencies, programs, and initiatives as the other members of the Puget Sound Federal Leadership Task Force determines necessary.

(B) Qualifications
Members appointed under this paragraph shall have experience and expertise in matters of restoration and protection of large watersheds and bodies of water, or related experience that will benefit the restoration and protection of the Puget Sound.

(C) Co-chairs
(i) In general
The following members of the Puget Sound Federal Leadership Task Force shall serve as Co-Chairs of the Puget Sound Federal Leadership Task Force:

(I) The representative of the National Oceanic and Atmospheric Administration.

(II) The Director of the Program Office.

(III) The representative of the Corps of Engineers.


(ii) Leadership
The Co-Chairs shall ensure the Puget Sound Federal Leadership Task Force completes its duties through robust discussion of all relevant issues. The Co-Chairs shall share leadership responsibilities equally.

(3) Duties
(A) General duties
The Puget Sound Federal Leadership Task Force shall—

(i) uphold Federal trust responsibilities to restore and protect resources crucial to Tribal treaty rights, including by carrying out government-to-government consultation with Indian tribes when requested by such tribes;

(ii) provide a venue for dialogue and coordination across all Federal agencies represented by a member of the Puget Sound Federal Leadership Task Force to align Federal resources for the purposes of carrying out the requirements of this section and all other Federal laws that contribute to the restoration and protection of the Puget Sound, including by—

(I) enabling and encouraging such agencies to act consistently with the objectives and priorities of the Action Agenda, the Salmon Recovery Plans, the Treaty Rights at Risk Initiative, and the Coastal Nonpoint Pollution Control Program;

(II) facilitating the coordination of Federal activities that impact such restoration and protection;

(III) facilitating the delivery of feedback given by such agencies to the Puget Sound Partnership during the development of the Action Agenda;

(IV) facilitating the resolution of interagency conflicts associated with such restoration and protection among such agencies;

(V) providing a forum for exchanging information among such agencies regarding activities being conducted, including obstacles or efficiencies found, during restoration and protection activities; and

(VI) promoting the efficient use of government resources in pursuit of such restoration and protection through coordination and collaboration, including by ensuring that the Federal efforts relating to the science necessary for such restoration and protection are consistent, and not duplicative, across the Federal Government;


(iii) catalyze public leaders at all levels to work together toward shared goals by demonstrating interagency best practices coming from such agencies;

(iv) provide advice and support on scientific and technical issues and act as a forum for the exchange of scientific information about the Puget Sound;

(v) identify and inventory Federal environmental research and monitoring programs related to the Puget Sound, and provide such inventory to the Puget Sound National Estuary Program Management Conference;

(vi) ensure that Puget Sound restoration and protection activities are as consistent as practicable with ongoing restoration and protection and related efforts in the Salish Sea that are being conducted by Canadian authorities, the Pacific Salmon Commission, and the International Joint Commission;

(vii) ensure that Puget Sound restoration and protection activities are consistent with national security interests;

(viii) establish any working groups or committees necessary to assist the Puget Sound Federal Leadership Task Force in its duties, including relating to public policy and scientific issues; and

(ix) raise national awareness of the significance of the Puget Sound.

(B) Puget Sound Federal Action Plan
(i) In general
Not later than 5 years after December 23, 2022, the Puget Sound Federal Leadership Task Force shall develop and approve a Federal Action Plan that leverages Federal programs across agencies and serves to coordinate diverse programs and priorities for the restoration and protection of the Puget Sound.

(ii) Revision of Puget Sound Federal Action Plan
Not less often than once every 5 years after the date of approval of the Federal Action Plan under clause (i), the Puget Sound Federal Leadership Task Force shall review, and revise as appropriate, the Federal Action Plan.

(C) Feedback by Federal agencies
In facilitating feedback under subparagraph (A)(ii)(III), the Puget Sound Federal Leadership Task Force shall request Federal agencies to consider, at a minimum, possible Federal actions within the Puget Sound region designed to—

(i) further the goals, targets, and actions of the Action Agenda, the Salmon Recovery Plans, the Treaty Rights at Risk Initiative, and the Coastal Nonpoint Pollution Control Program;

(ii) as applicable, implement and enforce this chapter, the Endangered Species Act of 1973 [16 U.S.C. 1531 et seq.], and all other Federal laws that contribute to the restoration and protection of the Puget Sound, including those that protect Tribal treaty rights;

(iii) prevent the introduction and spread of invasive species;

(iv) protect marine and wildlife habitats;

(v) protect, restore, and conserve forests, wetlands, riparian zones, and nearshore waters;

(vi) promote resilience to climate change and ocean acidification effects;

(vii) restore fisheries so that they are sustainable and productive;

(viii) preserve biodiversity;

(ix) restore and protect ecosystem services that provide clean water, filter toxic chemicals, and increase ecosystem resilience; and

(x) improve water quality, including by preventing and managing stormwater runoff, incorporating erosion control techniques and trash capture devices, using sustainable stormwater practices, and mitigating and minimizing nonpoint source pollution, including marine litter.

(4) Participation of State Advisory Committee and Puget Sound Tribal Management Conference
The Puget Sound Federal Leadership Task Force shall carry out its duties with input from, and in collaboration with, the State Advisory Committee and the Puget Sound Tribal Management Conference, including by seeking advice and recommendations on the actions, progress, and issues pertaining to the restoration and protection of the Puget Sound.

(5) Meetings
(A) Initial meeting
The Puget Sound Federal Leadership Task Force shall meet not later than 180 days after December 23, 2022—

(i) to determine if all Federal agencies are properly represented;

(ii) to establish the bylaws of the Puget Sound Federal Leadership Task Force;

(iii) to establish necessary working groups or committees; and

(iv) to determine subsequent meeting times, dates, and logistics.

(B) Subsequent meetings
After the initial meeting, the Puget Sound Federal Leadership Task Force shall meet, at a minimum, twice per year to carry out the duties of the Puget Sound Federal Leadership Task Force.

(C) Working group meetings
A meeting of any established working group or committee of the Puget Sound Federal Leadership Task Force shall not be considered a biannual meeting for purposes of subparagraph (B).

(D) Joint meetings
The Puget Sound Federal Leadership Task Force—

(i) shall offer to meet jointly with the Puget Sound National Estuary Program Management Conference and the Puget Sound Tribal Management Conference, at a minimum, once per year; and

(ii) may consider such a joint meeting to be a biannual meeting of the Puget Sound Federal Leadership Task Force for purposes of subparagraph (B).

(E) Quorum
A simple majority of the members of the Puget Sound Federal Leadership Task Force shall constitute a quorum.

(F) Voting
For the Puget Sound Federal Leadership Task Force to take an official action, a quorum shall be present, and at least a two-thirds majority of the members present shall vote in the affirmative.

(6) Puget Sound Federal Leadership Task Force procedures and advice
(A) Advisors
The Puget Sound Federal Leadership Task Force may seek advice and input from any interested, knowledgeable, or affected party as the Puget Sound Federal Leadership Task Force determines necessary to perform its duties.

(B) Compensation
A member of the Puget Sound Federal Leadership Task Force shall receive no additional compensation for service as a member on the Puget Sound Federal Leadership Task Force.

(C) Travel expenses
Travel expenses incurred by a member of the Puget Sound Federal Leadership Task Force in the performance of service on the Puget Sound Federal Leadership Task Force may be paid by the agency that the member represents.

(7) Puget Sound Federal Task Force
(A) In general
On December 23, 2022, the 2016 memorandum of understanding establishing the Puget Sound Federal Task Force shall cease to be effective.

(B) Use of previous work
The Puget Sound Federal Leadership Task Force shall, to the extent practicable, use the work product produced, relied upon, and analyzed by the Puget Sound Federal Task Force in order to avoid duplicating the efforts of the Puget Sound Federal Task Force.

(d) State Advisory Committee
(1) Establishment
There is established a State Advisory Committee.

(2) Membership
The State Advisory Committee shall consist of up to seven members designated by the governing body of the Puget Sound Partnership, in consultation with the Governor of Washington, who will represent Washington State agencies that have significant roles and responsibilities related to the restoration and protection of the Puget Sound.

(e) Puget Sound Federal Leadership Task Force biennial report on Puget Sound restoration and protection activities
(1) In general
Not later than 1 year after December 23, 2022, and biennially thereafter, the Puget Sound Federal Leadership Task Force, in collaboration with the Puget Sound Tribal Management Conference and the State Advisory Committee, shall submit to the President, Congress, the Governor of Washington, and the governing body of the Puget Sound Partnership a report that summarizes the progress, challenges, and milestones of the Puget Sound Federal Leadership Task Force relating to the restoration and protection of the Puget Sound.

(2) Contents
The report submitted under paragraph (1) shall include a description of the following:

(A) The roles and progress of each State, local government entity, and Federal agency that has jurisdiction in the Puget Sound region relating to meeting the identified objectives and priorities of the Action Agenda, the Salmon Recovery Plans, the Treaty Rights at Risk Initiative, and the Coastal Nonpoint Pollution Control Program.

(B) If available, the roles and progress of Tribal governments that have jurisdiction in the Puget Sound region relating to meeting the identified objectives and priorities of the Action Agenda, the Salmon Recovery Plans, the Treaty Rights at Risk Initiative, and the Coastal Nonpoint Pollution Control Program.

(C) A summary of specific recommendations concerning implementation of the Action Agenda and the Federal Action Plan, including challenges, barriers, and anticipated milestones, targets, and timelines.

(D) A summary of progress made by Federal agencies toward the priorities identified in the Federal Action Plan.

(f) Tribal rights and consultation
(1) Preservation of tribal treaty rights
Nothing in this section affects, or is intended to affect, any right reserved by treaty between the United States and one or more Indian tribes.

(2) Consultation
Nothing in this section affects any authorization or obligation of a Federal agency to consult with an Indian tribe under any other provision of law.

(g) Consistency
(1) In general
Actions authorized or implemented under this section shall be consistent with—

(A) the Salmon Recovery Plans;

(B) the Coastal Nonpoint Pollution Control Program; and

(C) the water quality standards of the State of Washington approved by the Administrator under section 1313 of this title.

(2) Federal actions
All Federal agencies represented on the Puget Sound Federal Leadership Task Force shall act consistently with the protection of Tribal, treaty-reserved rights and, to the greatest extent practicable given such agencies' existing obligations under Federal law, act consistently with the objectives and priorities of the Action Agenda, the Salmon Recovery Plans, the Treaty Rights at Risk Initiative, and the Coastal Nonpoint Pollution Control Program, when—

(A) conducting Federal agency activities within or outside the Puget Sound that affect any land or water use or natural resources of the Puget Sound region, including activities performed by a contractor for the benefit of a Federal agency;

(B) interpreting and enforcing regulations that impact the restoration and protection of the Puget Sound;

(C) issuing Federal licenses or permits that impact the restoration and protection of the Puget Sound; and

(D) granting Federal assistance to State, local, and Tribal governments for activities related to the restoration and protection of the Puget Sound.

"""

escaped_json_string = json.dumps(full_cwa_text, ensure_ascii=False)

subprocess.run("pbcopy", text=True, input=escaped_json_string, check=True)

print("Escaped JSON string copied to clipboard! ")