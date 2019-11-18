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
api.add_route(urls["path"]["get-user"], GetUserResource())
api.add_route(urls["path"]["add-meta-project"], AddMetaProjectResource())
api.add_route(urls["path"]["add-meta-milestone"], AddMetaMilestoneResource())
api.add_route(urls["path"]["add-meta-pulse"], AddMetaPulseResource())
api.add_route(urls["path"]["add-role"], AddRoleResource())
api.add_route(urls["path"]["add-locations"], AddLocationsResource())
api.add_route(urls["path"]["add-project"], AddProjectResource())
api.add_route(urls["path"]["add-milestone"], AddMilestoneResource())
api.add_route(urls["path"]["add-pulse"], AddPulseResource())
api.add_route(urls["path"]["get-roles"], GetRolesResource())
api.add_route(urls["path"]["get-projects"], GetProjectsResource())
api.add_route(urls["path"]["get-milestones"], GetMilestonesResource())
api.add_route(urls["path"]["get-pulses"], GetPulsesResource())
api.add_route(urls["path"]["get-meta-projects"], GetMetaProjectsResource())
api.add_route(urls["path"]["get-meta-milestones"], GetMetaMilestonesResource())
api.add_route(urls["path"]["get-meta-pulses"], GetMetaPulsesResource())
api.add_route(urls["path"]["get-my-pulses"], GetMyPulsesResource())
api.add_route(urls["path"]["update-pulse-timeline"], UpdatePulseTimelineResource())
api.add_route(urls["path"]["get-locations"], GetLocationsResource())
api.add_route(urls["path"]["update-base-location"], UpdateBaseLocationResource())
api.add_route(urls["path"]["add-travel"], AddTravelResource())
api.add_route(urls["path"]["add-non-availability"], AddNonAvailabilityResource())
api.add_route(urls["path"]["get-all-milestones"], GetAllMilestonesResource())
api.add_route(urls["path"]["get-user-pulses"], GetUserPulsesResource())

log.info("Circuit is up and running..")
