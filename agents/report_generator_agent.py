from collections import Counter

class ReportGeneratorAgent:
    """
    Agent to generate a professional threat model report with a summary.
    """
    def generate_report(self, risks):
        """
        Generates a detailed threat model report in Markdown format.

        Args:
            risks (list): A list of risks with their assessments.

        Returns:
            str: The generated report.
        """
        print("Generating professional report...")
        
        if not risks:
            return "# Threat Model Report\n\nNo risks were identified."

        # --- 1. Generate Summary Table ---
        risk_counts = Counter(risk['score'] for risk in risks)
        summary_table = "| Risk Level | Count |\n|------------|-------|\n"
        for level in ["Critical", "High", "Medium", "Low"]:
            summary_table += f"| {level} | {risk_counts[level]} |\n"

        # --- 2. Group and Sort Risks ---
        sorted_risks = sorted(risks, key=lambda x: ["Critical", "High", "Medium", "Low"].index(x['score']))
        
        # --- 3. Build the Report ---
        report = "# Threat Model Report\n\n"
        report += "## Executive Summary\n\n"
        report += summary_table + "\n"
        report += "## Detailed Findings\n\n"

        for risk in sorted_risks:
            report += f"### {risk['score']} - {risk['threat']}\n"
            report += f"- **Component ID**: `{risk['component_id']}`\n"
            report += f"- **Component Type**: `{risk['component_type']}`\n"
            report += f"- **Assessed Impact**: {risk['impact']}\n"
            report += f"- **Assessed Likelihood**: {risk['likelihood']}\n"
            report += f"- **Threat Framework**: {risk['framework']} ({risk['category']})\n\n"
            
        return report