def calculate_postmanbiri_scheme(total_boras=12, cost_per_pura=255, mini_packet_biris=13,
                                 transportation_cost=3300, selling_prices=[368, 375, 380]):
    """
    Calculates and displays scheme details for the Postman Biri scheme with dynamic cost adjustment.

    Args:
    - total_boras (int): Number of boras purchased (default is 12).
    - cost_per_pura (float): Base cost of 1 pura in ₹.
    - mini_packet_biris (int): Number of biris in one mini packet (default is 13).
    - transportation_cost (float): Total transportation cost in ₹.
    - selling_prices (list): List of selling prices to calculate profit/loss.

    Returns:
    - None: Displays the scheme table.
    """
    # Input for price adjustment
    adjustment_type = input("Does the company want to 'increase' or 'decrease' the base price? (Enter 'increase' or 'decrease'): ").strip().lower()
    adjustment_amount = float(input("Enter the adjustment amount in ₹: "))

    if adjustment_type == '+':
        adjusted_cost_per_pura = cost_per_pura + adjustment_amount
    elif adjustment_type == '_':
        adjusted_cost_per_pura = cost_per_pura - adjustment_amount
    else:
        print("Invalid adjustment type. Using base cost per pura.")
        adjusted_cost_per_pura = cost_per_pura

    # Constants
    biris_per_pura = 460
    puras_per_bora = 100
    total_scheme_biris = 78000

    # Step 1: Calculate total biriis
    total_biris_without_scheme = total_boras * puras_per_bora * biris_per_pura
    total_biris_with_scheme = total_biris_without_scheme + total_scheme_biris

    # Step 2: Calculate cost per biri
    total_cost = adjusted_cost_per_pura * puras_per_bora * total_boras
    total_cost_with_transport = total_cost + transportation_cost
    cost_per_biri = total_cost_with_transport / total_biris_with_scheme

    # Step 3: Adjust for reduced biri count in mini packets
    original_mini_packet_biris = 13
    company_savings_per_bora = 0
    if mini_packet_biris < original_mini_packet_biris:
        biris_reduced = (original_mini_packet_biris - mini_packet_biris) * (total_scheme_biris // original_mini_packet_biris)
        total_scheme_biris -= biris_reduced
        total_biris_with_scheme = total_biris_without_scheme + total_scheme_biris
        cost_per_biri = total_cost_with_transport / total_biris_with_scheme
        company_savings_per_bora = (original_mini_packet_biris - mini_packet_biris) * cost_per_biri * 3 * puras_per_bora

    # Step 4: Calculate costs
    cost_per_mini_packet = mini_packet_biris * cost_per_biri
    cost_of_3_mini_packets = 3 * cost_per_mini_packet
    cost_of_pura = biris_per_pura * cost_per_biri
    total_cost_pura_with_scheme = cost_of_pura + cost_of_3_mini_packets

    # Step 5: Calculate Postman Company profit/loss per bora and total profit
    company_profit_loss_per_bora = (adjusted_cost_per_pura - cost_per_pura) * puras_per_bora
    total_company_profit_loss = company_profit_loss_per_bora * total_boras

    # Step 6: Display scheme details
    print("\nPostman Biri Scheme Details")
    print(f"Base Cost per Pura: ₹{cost_per_pura}")
    print(f"Adjusted Cost per Pura: ₹{adjusted_cost_per_pura}")
    print(f"Adjustment Type: {adjustment_type.capitalize()} by ₹{adjustment_amount}")
    print(f"Total Cost for {total_boras} Boras: ₹{total_cost_with_transport:.2f}")
    print(f"Transportation Cost: ₹{transportation_cost:.2f}")
    print(f"Total Biriis Received (with scheme): {total_biris_with_scheme}")
    print(f"Cost per Biri: ₹{cost_per_biri:.3f}")
    print(f"Cost per Mini Packet ({mini_packet_biris} Biriis): ₹{cost_per_mini_packet:.2f}")
    print(f"Cost of 3 Mini Packets: ₹{cost_of_3_mini_packets:.2f}")
    print(f"Cost of 1 Pura (460 Biriis): ₹{cost_of_pura:.2f}")
    print(f"Total Cost of 1 Pura with Scheme: ₹{total_cost_pura_with_scheme:.2f}")
   # print(f"Company Profit/Loss per Bora (based on adjustment): ₹{company_profit_loss_per_bora:.2f}")
    #print(f"Total Company Profit/Loss for the Order: ₹{total_company_profit_loss:.2f}\n")

    # Step 7: Display selling price table
    print("Selling Price Analysis")
    print("| Selling Price (₹) | Profit/Loss (₹) | Profit/Loss (%) | Company Profit/Loss per Bora (₹) | Total Company Profit/Loss (₹) | Total User Profit (₹) |")
    print("|-------------------|------------------|-----------------|----------------------------------|------------------------------|----------------------|")
    for sp in selling_prices:
        profit_loss = sp - total_cost_pura_with_scheme
        profit_loss_percent = (profit_loss / total_cost_pura_with_scheme) * 100
        total_user_profit = profit_loss * puras_per_bora * total_boras
        print(f"| {sp:17} | {profit_loss:16.2f} | {profit_loss_percent:15.2f} | {company_profit_loss_per_bora:32.2f} | {total_company_profit_loss:28.2f} | {total_user_profit:20.2f} |")

# Example Usage
calculate_postmanbiri_scheme(total_boras=12, cost_per_pura=255, mini_packet_biris=13, transportation_cost=3300, selling_prices=[368, 375, 380])
