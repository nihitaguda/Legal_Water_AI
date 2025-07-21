import subprocess
import json

full_cwa_text = """
(a) Demonstration projects covering storm waters, advanced waste treatment and water purification methods, and joint treatment systems for municipal and industrial wastes
The Administrator is authorized to conduct in the Environmental Protection Agency, and to make grants to any State, municipality, or intermunicipal or interstate agency for the purpose of assisting in the development of—

(1) any project which will demonstrate a new or improved method of preventing, reducing, and eliminating the discharge into any waters of pollutants from sewers which carry storm water or both storm water and pollutants; or

(2) any project which will demonstrate advanced waste treatment and water purification methods (including the temporary use of new or improved chemical additives which provide substantial immediate improvements to existing treatment processes), or new or improved methods of joint treatment systems for municipal and industrial wastes;


and to include in such grants such amounts as are necessary for the purpose of reports, plans, and specifications in connection therewith.

(b) Demonstration projects for advanced treatment and environmental enhancement techniques to control pollution in river basins
The Administrator is authorized to make grants to any State or States or interstate agency to demonstrate, in river basins or portions thereof, advanced treatment and environmental enhancement techniques to control pollution from all sources, within such basins or portions thereof, including nonpoint sources, together with in stream 1 water quality improvement techniques.

(c) Research and demonstration projects for prevention of water pollution by industry
In order to carry out the purposes of section 1311 of this title, the Administrator is authorized to (1) conduct in the Environmental Protection Agency, (2) make grants to persons, and (3) enter into contracts with persons, for research and demonstration projects for prevention of pollution of any waters by industry including, but not limited to, the prevention, reduction, and elimination of the discharge of pollutants. No grant shall be made for any project under this subsection unless the Administrator determines that such project will develop or demonstrate a new or improved method of treating industrial wastes or otherwise prevent pollution by industry, which method shall have industrywide application.

(d) Accelerated and priority development of waste management and waste treatment methods and identification and measurement methods
In carrying out the provisions of this section, the Administrator shall conduct, on a priority basis, an accelerated effort to develop, refine, and achieve practical application of:

(1) waste management methods applicable to point and nonpoint sources of pollutants to eliminate the discharge of pollutants, including, but not limited to, elimination of runoff of pollutants and the effects of pollutants from inplace or accumulated sources;

(2) advanced waste treatment methods applicable to point and nonpoint sources, including inplace or accumulated sources of pollutants, and methods for reclaiming and recycling water and confining pollutants so they will not migrate to cause water or other environmental pollution; and

(3) improved methods and procedures to identify and measure the effects of pollutants on the chemical, physical, and biological integrity of water, including those pollutants created by new technological developments.

(e) Research and demonstration projects covering agricultural pollution and pollution from sewage in rural areas; dissemination of information
(1) The Administrator is authorized to (A) make, in consultation with the Secretary of Agriculture, grants to persons for research and demonstration projects with respect to new and improved methods of preventing, reducing, and eliminating pollution from agriculture, and (B) disseminate, in cooperation with the Secretary of Agriculture, such information obtained under this subsection, section 1254(p) of this title, and section 1314 of this title as will encourage and enable the adoption of such methods in the agricultural industry.

(2) The Administrator is authorized, (A) in consultation with other interested Federal agencies, to make grants for demonstration projects with respect to new and improved methods of preventing, reducing, storing, collecting, treating, or otherwise eliminating pollution from sewage in rural and other areas where collection of sewage in conventional, community-wide sewage collection systems is impractical, uneconomical, or otherwise infeasible, or where soil conditions or other factors preclude the use of septic tank and drainage field systems, and (B) in cooperation with other interested Federal and State agencies, to disseminate such information obtained under this subsection as will encourage and enable the adoption of new and improved methods developed pursuant to this subsection.

(f) Limitations
Federal grants under subsection (a) of this section shall be subject to the following limitations:

(1) No grant shall be made for any project unless such project shall have been approved by the appropriate State water pollution control agency or agencies and by the Administrator;

(2) No grant shall be made for any project in an amount exceeding 75 per centum of cost thereof as determined by the Administrator; and

(3) No grant shall be made for any project unless the Administrator determines that such project will serve as a useful demonstration for the purpose set forth in clause (1) or (2) of subsection (a).

(g) Maximum grants
Federal grants under subsections (c) and (d) of this section shall not exceed 75 per centum of the cost of the project.

(h) Authorization of appropriations
For the purpose of this section there is authorized to be appropriated $75,000,000 per fiscal year for the fiscal year ending June 30, 1973, the fiscal year ending June 30, 1974, and the fiscal year ending June 30, 1975, and from such appropriations at least 10 per centum of the funds actually appropriated in each fiscal year shall be available only for the purposes of subsection (e).

(i) Assistance for research and demonstration projects
The Administrator is authorized to make grants to a municipality to assist in the costs of operating and maintaining a project which received a grant under this section, section 1254 of this title, or section 1263 of this title prior to December 27, 1977, so as to reduce the operation and maintenance costs borne by the recipients of services from such project to costs comparable to those for projects assisted under subchapter II of this chapter.

(j) Assistance for recycle, reuse, and land treatment projects
The Administrator is authorized to make a grant to any grantee who received an increased grant pursuant to section 1282(a)(2) of this title. Such grant may pay up to 100 per centum of the costs of technical evaluation of the operation of the treatment works, costs of training of persons (other than employees of the grantee), and costs of disseminating technical information on the operation of the treatment works.

"""

escaped_json_string = json.dumps(full_cwa_text, ensure_ascii=False)

subprocess.run("pbcopy", text=True, input=escaped_json_string, check=True)

print("Escaped JSON string copied to clipboard! ")