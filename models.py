from enum import Enum
from typing import Annotated, Literal, Optional

from pydantic import BaseModel, Field


class BurdenLevel(str, Enum):
    LOW: Annotated[str, "Low burden - minimal additional work required"] = "low"
    MEDIUM: Annotated[str, "Medium burden - some additional work required"] = "medium"
    HIGH: Annotated[str, "High burden - significant additional work required"] = "high"

class Frequency(str, Enum):
    ANNUAL = "annual"
    SIX_MONTHLY = "six-monthly"
    QUARTERLY = "quarterly"
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    DAILY = "daily"
    ONGOING_AS_REQUIRED = "ongoing/as required"
    CONTINUOUS = "continuous"
    ONE_OFF = "one-off"

class UKDepartment(Enum):
    # Prime Minister's Office
    PRIME_MINISTERS_OFFICE = "Prime Minister's Office 10 Downing Street"

    # Ministerial Departments (24)
    ATTORNEY_GENERALS_OFFICE = "Attorney General's Office"
    CABINET_OFFICE = "Cabinet Office"
    DEPT_BUSINESS_TRADE = "Department for Business & Trade"
    DEPT_CULTURE_MEDIA_SPORT = "Department for Culture, Media & Sport"
    DEPT_EDUCATION = "Department for Education"
    DEPT_ENERGY_SECURITY_NET_ZERO = "Department for Energy Security & Net Zero"
    DEPT_ENVIRONMENT_FOOD_RURAL_AFFAIRS = "Department for Environment, Food & Rural Affairs"
    DEPT_SCIENCE_INNOVATION_TECHNOLOGY = "Department for Science, Innovation & Technology"
    DEPT_TRANSPORT = "Department for Transport"
    DEPT_WORK_PENSIONS = "Department for Work & Pensions"
    DEPT_HEALTH_SOCIAL_CARE = "Department of Health & Social Care"
    FOREIGN_COMMONWEALTH_DEVELOPMENT_OFFICE = "Foreign, Commonwealth & Development Office"
    HM_TREASURY = "HM Treasury"
    HOME_OFFICE = "Home Office"
    MINISTRY_OF_DEFENCE = "Ministry of Defence"
    MINISTRY_HOUSING_COMMUNITIES_LOCAL_GOVT = "Ministry of Housing, Communities & Local Government"
    MINISTRY_OF_JUSTICE = "Ministry of Justice"
    NORTHERN_IRELAND_OFFICE = "Northern Ireland Office"
    OFFICE_ADVOCATE_GENERAL_SCOTLAND = "Office of the Advocate General for Scotland"
    OFFICE_LEADER_HOUSE_COMMONS = "Office of the Leader of the House of Commons"
    OFFICE_LEADER_HOUSE_LORDS = "Office of the Leader of the House of Lords"
    SCOTLAND_OFFICE = "Scotland Office"
    UK_EXPORT_FINANCE = "UK Export Finance"
    WALES_OFFICE = "Wales Office"

    # Non-ministerial Departments (20)
    CHARITY_COMMISSION = "The Charity Commission"
    COMPETITION_MARKETS_AUTHORITY = "Competition and Markets Authority"
    CROWN_PROSECUTION_SERVICE = "Crown Prosecution Service"
    FOOD_STANDARDS_AGENCY = "Food Standards Agency"
    FORESTRY_COMMISSION = "Forestry Commission"
    GOVERNMENT_ACTUARYS_DEPARTMENT = "Government Actuary's Department"
    GOVERNMENT_LEGAL_DEPARTMENT = "Government Legal Department"
    HM_LAND_REGISTRY = "HM Land Registry"
    HM_REVENUE_CUSTOMS = "HM Revenue & Customs"
    NS_AND_I = "NS&I"
    NATIONAL_ARCHIVES = "The National Archives"
    NATIONAL_CRIME_AGENCY = "National Crime Agency"
    OFFICE_RAIL_ROAD = "Office of Rail and Road"
    OFGEM = "Ofgem"
    OFQUAL = "Ofqual"
    OFSTED = "Ofsted"
    SERIOUS_FRAUD_OFFICE = "Serious Fraud Office"
    SUPREME_COURT_UK = "Supreme Court of the United Kingdom"
    UK_STATISTICS_AUTHORITY = "UK Statistics Authority"
    WATER_SERVICES_REGULATION_AUTHORITY = "The Water Services Regulation Authority"

class LocationWithinLegislation(BaseModel):
    location_type: Literal["regulation", "schedule","paragraph"]
    location_number: int = Field(
        description="""
        The number of the location within the legislation document.
        This is a number that can be used to find the location of the duty within the legislation document.
        """
    )

    def __str__(self) -> str:
        return f"{self.location_type} {self.location_number}"

class CouncilDutyArea(str, Enum):
    GOVERNANCE_ADMIN_ELECTIONS: Annotated[str, "Organising elections, publishing council minutes, maintaining registers of interests, ensuring FOI compliance"] = "governance_admin_elections"

    CHILDREN_YOUNG_PEOPLE: Annotated[str, "Education, safeguarding children, providing school places, supporting SEND, delivering youth services"] = "children_young_people"

    ADULT_SOCIAL_CARE: Annotated[str, "Assessing care needs, providing home/residential care, safeguarding adults, supporting carers"] = "adult_social_care"

    PUBLIC_HEALTH: Annotated[str, "Delivering health checks, providing sexual health services, managing disease outbreaks, promoting healthy lifestyles"] = "public_health"

    HOUSING_HOMELESSNESS: Annotated[str, "Preventing homelessness, allocating social housing, enforcing housing standards, licensing HMOs"] = "housing_homelessness"

    COMMUNITY_SAFETY_CRIME_PREVENTION: Annotated[str, "Tackling anti-social behaviour, supporting domestic abuse victims, implementing Prevent duty, emergency planning"] = "community_safety_crime_prevention"

    ENVIRONMENTAL_HEALTH_PROTECTION: Annotated[str, "Food hygiene inspections, noise control, air quality monitoring, pest control"] = "environmental_health_protection"

    PLANNING_DEVELOPMENT: Annotated[str, "Preparing Local Plans, deciding planning applications, enforcing planning rules, protecting listed buildings"] = "planning_development"

    WASTE_RECYCLING: Annotated[str, "Collecting household waste, operating recycling centres, managing fly-tipping, promoting waste reduction"] = "waste_recycling"

    TRANSPORT_HIGHWAYS: Annotated[str, "Maintaining roads, managing parking, providing school transport, maintaining street lighting"] = "transport_highways"

    CULTURE_LEISURE_TOURISM: Annotated[str, "Running libraries, maintaining parks, operating leisure centres, promoting tourism"] = "culture_leisure_tourism"

    ECONOMIC_DEVELOPMENT_EMPLOYMENT: Annotated[str, "Supporting businesses, delivering training programmes, managing regeneration projects, working with LEPs"] = "economic_development_employment"

    FINANCE_REVENUES: Annotated[str, "Collecting council tax, administering benefits, managing budgets, providing financial advice"] = "finance_revenues"

    REGULATORY_SERVICES: Annotated[str, "Enforcing trading standards, licensing alcohol/taxis/gambling, inspecting food premises, regulating animal welfare"] = "regulatory_services"

    CLIMATE_CHANGE_SUSTAINABILITY: Annotated[str, "Developing climate action plans, promoting energy efficiency, managing flood risk, supporting green transport"] = "climate_change_sustainability"

    EQUALITY_DIVERSITY_INCLUSION: Annotated[str, "Complying with equality duty, promoting inclusive services, supporting community cohesion, addressing discrimination"] = "equality_diversity_inclusion"


class DutyAppliesTo(str, Enum):
    COUNTY_COUNCILS: Annotated[str, "Upper Tier: Education, social care, transport, libraries, waste disposal"] = "county_councils"

    DISTRICT_BOROUGH_CITY_COUNCILS: Annotated[str, "Lower Tier: Housing, local planning, waste collection, council tax collection"] = "district_borough_city_councils"

    UNITARY_AUTHORITIES: Annotated[str, "Single Tier: Responsible for all local government functions in their area, including education, housing, planning, and social care"] = "unitary_authorities"

    METROPOLITAN_BOROUGH_COUNCILS: Annotated[str, "Single Tier: Found in large urban areas like Manchester or Birmingham; provide all local services including social care, housing, and waste management"] = "metropolitan_borough_councils"

    LONDON_BOROUGH_COUNCILS: Annotated[str, "Single Tier: Deliver local services such as schools, housing, and social care within Greater London"] = "london_borough_councils"

    CITY_OF_LONDON_CORPORATION: Annotated[str, "Unique authority responsible for the Square Mile; provides local authority services and manages the City's business district"] = "city_of_london_corporation"

    GREATER_LONDON_AUTHORITY: Annotated[str, "Strategic authority for Greater London; oversees transport (TfL), policing (Met Police), and fire services"] = "greater_london_authority"

    COMBINED_AUTHORITIES: Annotated[str, "Strategic regional bodies (like Greater Manchester Combined Authority); responsible for transport, economic development, and housing"] = "combined_authorities"

    PARISH_TOWN_COMMUNITY_COUNCILS: Annotated[str, "Managing local amenities like parks, allotments, bus shelters, and community centres; commenting on planning applications"] = "parish_town_community_councils"

class MonitoredBy(BaseModel):
    is_monitored: bool = Field(description="Whether the duty is monitored by a government department or arms length body at all, or not")
    department: Optional[UKDepartment] = Field(default=None,description="The government department responsible for monitoring the delivery of this duty, if applicable")
    arms_length_body: Optional[str] = Field(default=None,description="The arms length body responsible for monitoring the delivery of this duty, if applicable")

    def __str__(self) -> str:
        if self.is_monitored:
            if self.department:
                return f"Monitored by {self.department}"
            elif self.arms_length_body:
                return f"Monitored by {self.arms_length_body}"
        return "Not monitored"

class ConfidenceLevels(BaseModel):
    legislation_title: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    legislation_link: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    location_within_legislation: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    department_lead: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    key_policy_or_theme: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    duty_description: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    duty_applies_to: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    affected_groups: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    resources_required: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    frequency: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    burden_level: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    burden_reduction_suggestions: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    is_monitored: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    enforcement_mechanisms: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    performance_impact: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]
    linked_duties: Literal["Low", "Low-Medium","Medium", "Medium-High", "High"]

class Duty(BaseModel):
    legislation_title: str
    legislation_link: str
    location_within_legislation: list[LocationWithinLegislation] = Field(
        description="""
        The location(s) of the duty within the legislation document.
        If you're not sure about the location type, default to regulation.
        If you can see a hierarchy, for example something in Schedule 1, then paragraph 2, then you should record the location type as paragraph and the location number as 2.

        Almost always there will only be a single location, but you can use a list if a duty is spread across multiple locations, or if there are multiple sub-duties split across locations that are better captured as a single duty.
        """
    )
    department_lead: UKDepartment = Field(
        description="""
        The government department that created the duty. You can often look at the signature to determine this.
        """
    )
    key_policy_or_theme: CouncilDutyArea = Field(
        description = "Council duty areas that constrain where specific duties should fall."
    )
    duty_description: str = Field(
        description="""
        Detailed description of **what the duty requires the authority to do**. 
        Should include sufficient context and detail, even if it references other legislation.
        This is the most important field - be comprehensive and clear.
        """
    )
    duty_title: str = Field(
        description="A short title for the duty"
    )
    duty_applies_to: list[DutyAppliesTo] = Field(
        description = "Council tiers to which duties might apply"
    )
    affected_groups: str = Field(
        description="""Does this duty affect residents universally or does it target specific groups or circumstances? If targeted, describe which specific groups are affected (e.g., 'vulnerable young people aged 16-17', 'children in state schools')"""
    )
    resources_required: list[str] = Field(
        description="""What resources are required to perform this duty? (e.g., staff, equipment, funding, systems). Where possible take from this list below, but use your own judgement if the duty is not listed:
        Human Resources: e.g. Social workers, legal advisors, administrative staff, community outreach officers, legal resource
        Digital and IT Resources: e.g. Case management systems, GIS tools, secure data storage, online service portals
        Physical Infrastructure: e.g. Access to medical facilities, community centres, emergency accommodation, public transport hubs
        Knowledge and Information Resources: e.g. Legal databases, policy manuals, training materials, research access, public engagement tools
        Financial Resources: e.g. Core funding, grants, procurement budgets, contingency funds
        Partnership and External Support: e.g. Contracts with providers, NHS and police collaboration, shared services, voluntary sector links
        Monitoring and Evaluation Tools: e.g. Performance dashboards, audit frameworks, complaints systems, risk assessment tools
        """
    )
    frequency: Frequency = Field(
        description="How often the authority must perform this duty. Look for specific intervals mentioned in the legislation. If no specific interval is mentioned, it's usually 'Ongoing/as required'."
    )
    burden_level: BurdenLevel = Field(
        description="What level of burden might this duty place on local authorities?"
    )
    burden_reduction_suggestions: list[str] = Field(
        description="Suggestions for how this duty could be modified to reduce administrative burden"
    )
    is_monitored: MonitoredBy = Field(
        description="""
        Whether and how the delivery of this duty is monitored
        (e.g., 'Yes - through Ofsted inspections', 'No specific monitoring mentioned')

        Often the duty is monitored by a Government department or arms length body
        """
    )
    enforcement_mechanisms: list[str] = Field(
        description="""
        What enforcement mechanisms exist for this duty? (e.g. Legal enforcement, Criminal penalties for breaches, Judicial review, financial penalties, public complaints, whistleblowing, etc.)
        """
    )
    performance_impact: str = Field(
        description="""
        How failure to deliver this duty affects local authority performance 
        (e.g., audit consequences, legal repercussions, inspection failures, etc.)
        """
    )
    linked_duties: list[str] = Field(
        description="""
        Other duties that are linked to or dependent on this duty, 
        particularly references to other pieces of legislation
        """
    )

    confidence_levels: ConfidenceLevels = Field(
        description="""
        How confident are you in the accuracy of the fields you've filled out?
        Low: If someone else were to fill out this field, it's likely they'd get a different answer.
        Medium: If someone else were to fill out this field, it's likely they'd get a similar answer.
        High: If someone else were to fill out this field, they will get the same answer.
        This is a measure of how confident we are in the accuracy of the field.
        """
    )

class Duties(BaseModel):
    reasoning: str = Field(
        description="""
        A brief summary of your thought process before extracting the relevant duties. Include anything you need to think carefully about before extracting the duties.
        """
    )

    duties: list[Duty]

class ShouldExtractDuty(BaseModel):
    reasoning: str = Field(
        description="""
        A brief summary of your thought process before deciding whether to extract the duty. Include anything you need to think carefully about before extracting the duty.
        """
    )
    should_extract: bool = Field(
        description="""
        Whether you think the duty should be extracted or not.
        """
    )

class Theme(BaseModel):
    theme_reasoning: str = Field(
        description="""A brief summary of your thought process before extracting the theme."""
    )

    theme_title: str = Field(
        description = "The title of the theme."
    )
    theme_description: str = Field(
        description = "The description of the theme."
    )
    theme_duties: list[str] = Field(
        description = "The duty ids that are related to this theme."
    )

class Themes(BaseModel):
    reasoning: str = Field(
        description="""A brief summary of your thought process before extracting the overall themes."""
    )

    themes: list[Theme]
