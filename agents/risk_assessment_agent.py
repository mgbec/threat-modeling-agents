class RiskAssessmentAgent:
    """
    Agent to assess the risks of identified threats with more detailed logic.
    """
    def assess_risks(self, threats):
        """
        Assesses the risks of identified threats based on their category.

        Args:
            threats (list): A list of identified threats.

        Returns:
            list: A list of risks with a detailed assessment.
        """
        print("Assessing risks with enhanced logic...")
        risks = []
        
        # A knowledge base for risk scoring based on threat category.
        # This defines the potential impact and likelihood for different types of attacks.
        risk_definitions = {
            "Credential Access": {"impact": "High", "likelihood": "High"},
            "Initial Access": {"impact": "High", "likelihood": "Medium"},
            "Impact": {"impact": "High", "likelihood": "Low"},
            "Information Disclosure": {"impact": "Medium", "likelihood": "Medium"},
            "Denial of Service": {"impact": "Medium", "likelihood": "High"},
            "Spoofing": {"impact": "Low", "likelihood": "Medium"},
            "Default": {"impact": "Low", "likelihood": "Low"} # Fallback for unknown categories
        }

        for threat in threats:
            category = threat.get("category", "Default")
            assessment = risk_definitions.get(category, risk_definitions["Default"])
            
            risk = threat.copy()
            risk["impact"] = assessment["impact"]
            risk["likelihood"] = assessment["likelihood"]
            
            # Determine final score based on impact and likelihood
            if risk["impact"] == "High" and risk["likelihood"] == "High":
                risk["score"] = "Critical"
            elif risk["impact"] == "High" or risk["likelihood"] == "High":
                risk["score"] = "High"
            elif risk["impact"] == "Medium" and risk["likelihood"] == "Medium":
                risk["score"] = "Medium"
            else:
                risk["score"] = "Low"
                
            risks.append(risk)
            
        return risks