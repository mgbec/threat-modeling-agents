import argparse
import os
from agents.vision_architecture_parser_agent import VisionArchitectureParserAgent
from agents.threat_modeling_agent import ThreatModelingAgent
from agents.risk_assessment_agent import RiskAssessmentAgent
from agents.report_generator_agent import ReportGeneratorAgent

def main():
    """
    Main function to orchestrate the threat modeling process.
    """
    parser = argparse.ArgumentParser(description="Threat Modeler")
    parser.add_argument("--image_path", help="Path to the architecture diagram image.", required=True)
    parser.add_argument("--api_key", help="Your Google API Key for Gemini.", required=True)
    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"Error: Image path not found at {args.image_path}")
        return

    # 1. Vision Architecture Parser Agent
    vision_parser_agent = VisionArchitectureParserAgent(api_key=args.api_key)
    architecture_data = vision_parser_agent.parse_architecture(args.image_path)

    if not architecture_data:
        print("Error: Could not parse architecture from the image.")
        return
    
    print("Architecture Data:", architecture_data)

    # 2. Threat Modeling Agent
    threat_modeler_agent = ThreatModelingAgent()
    threats = threat_modeler_agent.model_threats(architecture_data)

    print("Threats:", threats)

    # 3. Risk Assessment Agent
    risk_assessment_agent = RiskAssessmentAgent()
    risks = risk_assessment_agent.assess_risks(threats)
    
    print("Risks:", risks)

    # 4. Report Generator Agent
    report_generator_agent = ReportGeneratorAgent()
    report = report_generator_agent.generate_report(risks)

    with open("Threat_Model_Report.md", "w") as f:
        f.write(report)

    print("Threat model report generated successfully at Threat_Model_Report.md")

if __name__ == "__main__":
    main()