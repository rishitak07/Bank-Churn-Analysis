-- 1. Overall churn rate
SELECT COUNT(*) AS total_customers,
       SUM(churn_flag) AS churned,
       ROUND(100 * AVG(churn_flag), 2) AS churn_rate
FROM bank_churn;

-- 2. Churn by geography
SELECT geography,
       COUNT(*) AS customers,
       SUM(churn_flag) AS churned,
       ROUND(100 * AVG(churn_flag), 2) AS churn_rate
FROM bank_churn
GROUP BY geography
ORDER BY churn_rate DESC;
-- 3. Churn by age group
SELECT age_group, COUNT(*) AS customers,
       ROUND(100 * AVG(churn_flag), 2) AS churn_rate
FROM bank_churn
GROUP BY age_group
ORDER BY churn_rate DESC;

-- 4. Churn by number of products
SELECT numofproducts, COUNT(*) AS customers,
       ROUND(100 * AVG(churn_flag), 2) AS churn_rate
FROM bank_churn
GROUP BY numofproducts
ORDER BY numofproducts;

-- 5. Churn by active status
SELECT active_status, COUNT(*) AS customers,
       ROUND(100 * AVG(churn_flag), 2) AS churn_rate
FROM bank_churn
GROUP BY active_status;

-- 6. Churn by gender
SELECT gender, COUNT(*) AS customers,
       ROUND(100 * AVG(churn_flag), 2) AS churn_rate
FROM bank_churn
GROUP BY gender;

-- 7. Churn by balance band
SELECT balance_band, COUNT(*) AS customers,
       ROUND(100 * AVG(churn_flag), 2) AS churn_rate
FROM bank_churn
GROUP BY balance_band
ORDER BY churn_rate DESC;

-- 8. Churn by tenure group
SELECT tenure_group, COUNT(*) AS customers,
       ROUND(100 * AVG(churn_flag), 2) AS churn_rate
FROM bank_churn
GROUP BY tenure_group;

-- 9. High-risk segment: inactive + age 40+ + Germany
SELECT COUNT(*) AS customers,
       ROUND(100 * AVG(churn_flag), 2) AS churn_rate
FROM bank_churn
WHERE active_status = 'Inactive'
  AND age >= 40
  AND geography = 'Germany';