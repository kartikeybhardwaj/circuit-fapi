import falcon
from falcon_cors import CORS

from utils.log import logger as log
from constants.urls import urls
from middleware.middleware import Middleware
from source.extras.status import StatusResource
from source.user.get_user import GetUserResource
from source.project.add_meta_project import AddMetaProjectResource
from source.milestone.add_meta_milestone import AddMetaMilestoneResource
from source.pulse.add_meta_pulse import AddMetaPulseResource
from source.role.add_role import AddRoleResource
from source.location.add_locations import AddLocationsResource
from source.project.add_project import AddProjectResource
from source.milestone.add_milestone import AddMilestoneResource
from source.pulse.add_pulse import AddPulseResource
from source.role.get_roles import GetRolesResource
from source.project.get_projects import GetProjectsResource
from source.milestone.get_milestones import GetMilestonesResource
from source.pulse.get_pulses import GetPulsesResource
from source.project.get_meta_projects import GetMetaProjectsResource
from source.milestone.get_meta_milestones import GetMetaMilestonesResource
from source.pulse.get_meta_pulses import GetMetaPulsesResource
from source.pulse.get_my_pulses import GetMyPulsesResource
from source.pulse.update_pulse_timeline import UpdatePulseTimelineResource
from source.location.get_locations import GetLocationsResource
from source.location.update_base_location import UpdateBaseLocationResource
from source.user.add_travel import AddTravelResource
from source.user.add_non_availability import AddNonAvailabilityResource
from source.milestone.get_all_milestones import GetAllMilestonesResource
from source.pulse.get_user_pulses import GetUserPulsesResource

cors = CORS(allow_origins_list=["http://localhost:4200"],
            allow_credentials_all_origins=True,
            allow_all_headers=True,
            allow_all_methods=True)

api = falcon.API(middleware=[
    cors.middleware,
    Middleware()
])

api.add_route("/", StatusResource())
api.add_route(urls["paths"]["get-user"], GetUserResource())
api.add_route(urls["paths"]["add-meta-project"], AddMetaProjectResource())
api.add_route(urls["paths"]["add-meta-milestone"], AddMetaMilestoneResource())
api.add_route(urls["paths"]["add-meta-pulse"], AddMetaPulseResource())
api.add_route(urls["paths"]["add-role"], AddRoleResource())
api.add_route(urls["paths"]["add-locations"], AddLocationsResource())
api.add_route(urls["paths"]["add-project"], AddProjectResource())
api.add_route(urls["paths"]["add-milestone"], AddMilestoneResource())
api.add_route(urls["paths"]["add-pulse"], AddPulseResource())
api.add_route(urls["paths"]["get-roles"], GetRolesResource())
api.add_route(urls["paths"]["get-projects"], GetProjectsResource())
api.add_route(urls["paths"]["get-milestones"], GetMilestonesResource())
api.add_route(urls["paths"]["get-pulses"], GetPulsesResource())
api.add_route(urls["paths"]["get-meta-projects"], GetMetaProjectsResource())
api.add_route(urls["paths"]["get-meta-milestones"], GetMetaMilestonesResource())
api.add_route(urls["paths"]["get-meta-pulses"], GetMetaPulsesResource())
api.add_route(urls["paths"]["get-my-pulses"], GetMyPulsesResource())
api.add_route(urls["paths"]["update-pulse-timeline"], UpdatePulseTimelineResource())
api.add_route(urls["paths"]["get-locations"], GetLocationsResource())
api.add_route(urls["paths"]["update-base-location"], UpdateBaseLocationResource())
api.add_route(urls["paths"]["add-travel"], AddTravelResource())
api.add_route(urls["paths"]["add-non-availability"], AddNonAvailabilityResource())
api.add_route(urls["paths"]["get-all-milestones"], GetAllMilestonesResource())
api.add_route(urls["paths"]["get-user-pulses"], GetUserPulsesResource())

log.info("Circuit is up and running..")
