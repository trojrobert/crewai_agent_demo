from datetime import date
from textwrap import dedent

from crewai import Task


def analyze_destination_task(agent, origin, cities, interests, range):
    """
    Creates a task for analyzing and selecting the optimal destination city
    based on multiple criteria including weather, events, and costs.
    """
    return Task(
        description=dedent(
            f"""
                Analyze and select the best city for the trip based 
                on specific criteria such as weather patterns, seasonal
                events, and travel costs. This task involves comparing
                multiple cities, considering factors like current weather
                conditions, upcoming cultural or seasonal events, and
                overall travel expenses. 
                
                Your final answer must be a detailed
                report on the chosen city, and everything you found out
                about it, including the actual flight costs, weather 
                forecast and attractions.

                Traveling from: {origin}
                City Options: {cities}
                Trip Date: {range}
                Traveler Interests: {interests}
            """
        ),
        agent=agent,
        expected_output="Detailed report on the chosen city including flight costs, weather forecast, and attractions",
    )


def city_guide_task(agent, cities, interests, range):
    """
    Creates a task for gathering detailed local knowledge and creating
    a comprehensive city guide with insider information.
    """
    return Task(
        description=dedent(
            f"""
            As a local expert on this city you must compile an 
            in-depth guide for someone traveling there and wanting 
            to have THE BEST trip ever!
            Gather information about key attractions, local customs,
            special events, and daily activity recommendations.
            Find the best spots to go to, the kind of place only a
            local would know.
            This guide should provide a thorough overview of what 
            the city has to offer, including hidden gems, cultural
            hotspots, must-visit landmarks, weather forecasts, and
            high level costs.
            
            The final answer must be a comprehensive city guide, 
            rich in cultural insights and practical tips, 
            tailored to enhance the travel experience.

            Trip Date: {range}
            Traveling to: {cities}
            Traveler Interests: {interests}
        """
        ),
        agent=agent,
        expected_output="Comprehensive city guide including hidden gems, cultural hotspots, and practical travel tips",
    )


def create_itinerary_task(agent, cities, interests, range):
    """
    Creates a task for developing a comprehensive day-by-day travel itinerary
    with specific recommendations and practical details.
    """
    return Task(
        description=dedent(
            f"""
            Expand this guide into a full 7-day travel 
            itinerary with detailed per-day plans, including 
            weather forecasts, places to eat, packing suggestions, 
            and a budget breakdown.
            
            You MUST suggest actual places to visit, actual hotels 
            to stay and actual restaurants to go to.
            
            This itinerary should cover all aspects of the trip, 
            from arrival to departure, integrating the city guide
            information with practical travel logistics.
            
            Your final answer MUST be a complete expanded travel plan,
            formatted as markdown, encompassing a daily schedule,
            anticipated weather conditions, recommended clothing and
            items to pack, and a detailed budget, ensuring THE BEST
            TRIP EVER. Be specific and give it a reason why you picked
            each place, what makes them special!

            Trip Date: {range}
            Traveling to: {cities}
            Traveler Interests: {interests}
        """
        ),
        agent=agent,
        expected_output="Complete expanded travel plan with daily schedule, weather conditions, packing suggestions, and budget breakdown",
    )
