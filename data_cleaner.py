import subprocess
import json

full_cwa_text = """
(a) Restoration and maintenance of chemical, physical and biological integrity of Nation's waters; national goals for achievement of objective
The objective of this chapter is to restore and maintain the chemical, physical, and biological integrity of the Nation's waters. In order to achieve this objective it is hereby declared that, consistent with the provisions of this chapter—

(1) it is the national goal that the discharge of pollutants into the navigable waters be eliminated by 1985;

(2) it is the national goal that wherever attainable, an interim goal of water quality which provides for the protection and propagation of fish, shellfish, and wildlife and provides for recreation in and on the water be achieved by July 1, 1983;

(3) it is the national policy that the discharge of toxic pollutants in toxic amounts be prohibited;

(4) it is the national policy that Federal financial assistance be provided to construct publicly owned waste treatment works;

(5) it is the national policy that areawide waste treatment management planning processes be developed and implemented to assure adequate control of sources of pollutants in each State;

(6) it is the national policy that a major research and demonstration effort be made to develop technology necessary to eliminate the discharge of pollutants into the navigable waters, waters of the contiguous zone, and the oceans; and

(7) it is the national policy that programs for the control of nonpoint sources of pollution be developed and implemented in an expeditious manner so as to enable the goals of this chapter to be met through the control of both point and nonpoint sources of pollution.

(b) Congressional recognition, preservation, and protection of primary responsibilities and rights of States
It is the policy of the Congress to recognize, preserve, and protect the primary responsibilities and rights of States to prevent, reduce, and eliminate pollution, to plan the development and use (including restoration, preservation, and enhancement) of land and water resources, and to consult with the Administrator in the exercise of his authority under this chapter. It is the policy of Congress that the States manage the construction grant program under this chapter and implement the permit programs under sections 1342 and 1344 of this title. It is further the policy of the Congress to support and aid research relating to the prevention, reduction, and elimination of pollution and to provide Federal technical services and financial aid to State and interstate agencies and municipalities in connection with the prevention, reduction, and elimination of pollution.

(c) Congressional policy toward Presidential activities with foreign countries
It is further the policy of Congress that the President, acting through the Secretary of State and such national and international organizations as he determines appropriate, shall take such action as may be necessary to insure that to the fullest extent possible all foreign countries shall take meaningful action for the prevention, reduction, and elimination of pollution in their waters and in international waters and for the achievement of goals regarding the elimination of discharge of pollutants and the improvement of water quality to at least the same extent as the United States does under its laws.

(d) Administrator of Environmental Protection Agency to administer chapter
Except as otherwise expressly provided in this chapter, the Administrator of the Environmental Protection Agency (hereinafter in this chapter called "Administrator") shall administer this chapter.

(e) Public participation in development, revision, and enforcement of any regulation, etc.
Public participation in the development, revision, and enforcement of any regulation, standard, effluent limitation, plan, or program established by the Administrator or any State under this chapter shall be provided for, encouraged, and assisted by the Administrator and the States. The Administrator, in cooperation with the States, shall develop and publish regulations specifying minimum guidelines for public participation in such processes.

(f) Procedures utilized for implementing chapter
It is the national policy that to the maximum extent possible the procedures utilized for implementing this chapter shall encourage the drastic minimization of paperwork and interagency decision procedures, and the best use of available manpower and funds, so as to prevent needless duplication and unnecessary delays at all levels of government.

(g) Authority of States over water
It is the policy of Congress that the authority of each State to allocate quantities of water within its jurisdiction shall not be superseded, abrogated or otherwise impaired by this chapter. It is the further policy of Congress that nothing in this chapter shall be construed to supersede or abrogate rights to quantities of water which have been established by any State. Federal agencies shall co-operate with State and local agencies to develop comprehensive solutions to prevent, reduce and eliminate pollution in concert with programs for managing water resources.

"""

# Convert text to a JSON-safe string
escaped_json_string = json.dumps(full_cwa_text.strip(), ensure_ascii=False)

# Copy to clipboard using macOS pbcopy
try:
    subprocess.run("pbcopy", text=True, input=escaped_json_string, check=True)
    print("✅ Escaped JSON string copied to clipboard!")
except Exception as e:
    print(f"❌ Error copying to clipboard: {e}")
