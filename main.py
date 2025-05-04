import os
from dotenv import load_dotenv
from tasks import OsintAnalysisTask
from agents import OsintAgents
from crewai import Crew

load_dotenv()

os.environ["EXA_API_KEY"] = os.getenv("EXA_API_KEY")


def main():
    tasks = OsintAnalysisTask()
    agents = OsintAgents()

    print("## Welcome to Osint Anaysis of Company")
    print('-------------------------------')
    company = input("Enter the name of company\n")
	
    # Create Agents
    Information_agent = agents.CompanyInfo_agent()
    WebsiteAnalyst = agents.WebsiteAnalysis_agent()
    NetworkAnalyst = agents.NetworkAnalysis_agent()
    SocialMediaAndContact = agents.SocialMediaAndContact_agent()
    SearchEngineIntelligence = agents.SearchEngineIntelligence_agent()
    BusinessInformation = agents.BusinessInformation_agent()
    RegulatoryLegalTechnicalFootprint = agents.RegulatoryLegalTechnicalFootprint_agent()
    IntellectualProperty = agents.IntellectualProperty_agent()
    EmployeeHiringInformation = agents.EmployeeHiringInformation_agent()
    CommunityPublicPerception = agents.CommunityPublicPerception_agent()
    OsintReporter = agents.OSINTReportGenerator_agent()


    # Create Tasks
    information = tasks.CompanyInfo_task(Information_agent , company)
    website_analysis = tasks.WebsiteAnalysis_task(WebsiteAnalyst, company)
    network_analysis = tasks.NetworkAnalysis_task(NetworkAnalyst, company)
    social_media_and_contact = tasks.SocialMediaAndContact_task(SocialMediaAndContact, company)
    search_engine_intelligence = tasks.SearchEngineIntelligence_task(SearchEngineIntelligence, company)
    business_information = tasks.BusinessInformation_task(BusinessInformation, company)
    regulatory_legal_technical_footprint = tasks.RegulatoryLegalTechnicalFootprint_task(RegulatoryLegalTechnicalFootprint, company)
    intellectual_property = tasks.IntellectualProperty_task(IntellectualProperty, company)
    employee_hiring_information = tasks.EmployeeHiringInformation_task(EmployeeHiringInformation, company)
    community_public_perception = tasks.CommunityPublicPerception_task(CommunityPublicPerception, company)
    summary_and_briefing = tasks.OSINTReportGenerator_task(OsintReporter, company)

    # create context
    summary_and_briefing.context = [
        information,
        website_analysis,
        network_analysis,
        social_media_and_contact,
        search_engine_intelligence,
        business_information,
        regulatory_legal_technical_footprint,
        intellectual_property,
        employee_hiring_information,
        community_public_perception
    ]
	
    # Create Crew responsible for Copy
    crew = Crew(
        agents=[
            Information_agent,
            WebsiteAnalyst,
        NetworkAnalyst,
        SocialMediaAndContact,
        SearchEngineIntelligence,
        BusinessInformation,
        RegulatoryLegalTechnicalFootprint,
        IntellectualProperty,
        EmployeeHiringInformation,
        CommunityPublicPerception,
            OsintReporter
        ],
        tasks=[
            information,
            website_analysis,
        network_analysis,
        social_media_and_contact,
        search_engine_intelligence,
        business_information,
        regulatory_legal_technical_footprint,
        intellectual_property,
        employee_hiring_information,
        community_public_perception,
        summary_and_briefing
        ]
    )
	
    result = crew.kickoff()


    # Print results
    print("\n\n################################################")
    print("## Here is the result")
    print("################################################\n")
    print(result)


if __name__ == "__main__":
    main()
