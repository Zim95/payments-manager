# Phase 1: Order Creation & Payment Processing
1. User selects a subscription plan (SubscriptionType)
   ↓
2. Create Order record with:
   - status: PENDING
   - subscription_type_id: selected plan
   - subscription_id: NULL (for new) or existing subscription ID (for renewal/upgrade)
   - amount: from SubscriptionType
   - payment_provider_id: NULL (will be set after Razorpay order creation)
   ↓
3. Create Razorpay Order using Razorpay API
   ↓
4. Update Order record with:
   - payment_provider_id: Razorpay order ID
   - payment_method: "razorpay"
   ↓
5. Return payment details to frontend for Razorpay checkout


# Phase 2: Payment Success Handling
1. Razorpay webhook receives payment success
   ↓
2. Verify payment signature and status
   ↓
3. Update Order record:
   - status: PAID
   - paid_at: current timestamp
   ↓
4. Handle Subscription logic:

   IF new subscription (subscription_id is NULL):
   - Create new Subscription record
   - Set status: ACTIVE
   - Set valid_until: current_date + duration_days
   - Update Order.subscription_id with new subscription ID

   IF renewal/upgrade (subscription_id exists):
   - Update existing Subscription record
   - Extend valid_until or change subscription_type_id
   - Set status: ACTIVE


# Phase 3: Payment Failure Handling
1. Razorpay webhook receives payment failure
   ↓
2. Update Order record:
   - status: FAILED
   ↓
3. Keep Subscription unchanged (if renewal) or don't create (if new)
