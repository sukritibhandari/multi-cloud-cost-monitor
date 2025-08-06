from aws.aws_cost import fetch_aws_costs
from azure.azure_cost import fetch_azure_costs
from gcp.gcp_cost import fetch_gcp_costs

def main():
    print("Fetching multi-cloud billing data...")
    fetch_aws_cost()
    fetch_azure_cost()
    fetch_gcp_cost()
    print("Done.")

if __name__ == "__main__":
    main()