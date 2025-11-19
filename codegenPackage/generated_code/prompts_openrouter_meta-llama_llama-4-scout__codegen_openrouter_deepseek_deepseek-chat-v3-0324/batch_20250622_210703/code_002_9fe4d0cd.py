"""
Generated Code Metadata:
========================
Original URL: https://tokenpocket-bkw.pages.dev
Prompt: "Generate a code snippet for a Christmas promotion on a TokenPocket-like interface."
Generated: DETERMINISTIC_9fe4d0cd20d3dfc7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Image } from 'react-native';
import { useNavigation } from '@react-navigation/native';

interface ChristmasPromotionProps {
  promotionEndDate: Date;
}

const ChristmasPromotion: React.FC<ChristmasPromotionProps> = ({ promotionEndDate }) => {
  const navigation = useNavigation();
  const [timeLeft, setTimeLeft] = useState<string>('');
  const [isPromotionActive, setIsPromotionActive] = useState<boolean>(true);

  useEffect(() => {
    const calculateTimeLeft = () => {
      const now = new Date();
      const difference = promotionEndDate.getTime() - now.getTime();

      if (difference <= 0) {
        setIsPromotionActive(false);
        return;
      }

      const days = Math.floor(difference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((difference / (1000 * 60 * 60)) % 24);
      const minutes = Math.floor((difference / 1000 / 60) % 60);
      const seconds = Math.floor((difference / 1000) % 60);

      setTimeLeft(`${days}d ${hours}h ${minutes}m ${seconds}s`);
    };

    const timer = setInterval(calculateTimeLeft, 1000);
    calculateTimeLeft();

    return () => clearInterval(timer);
  }, [promotionEndDate]);

  const handlePromotionPress = () => {
    if (!isPromotionActive) return;
    navigation.navigate('PromotionDetails');
  };

  if (!isPromotionActive) return null;

  return (
    <TouchableOpacity 
      style={styles.container}
      onPress={handlePromotionPress}
      activeOpacity={0.8}
    >
      <Image
        source={require('../assets/christmas_banner.png')}
        style={styles.banner}
        resizeMode="contain"
      />
      <View style={styles.textContainer}>
        <Text style={styles.title}>Christmas Special!</Text>
        <Text style={styles.subtitle}>Limited-time offers on selected tokens</Text>
        <Text style={styles.timer}>Ends in: {timeLeft}</Text>
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#E51F45',
    borderRadius: 12,
    padding: 16,
    margin: 16,
    flexDirection: 'row',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
    elevation: 3,
  },
  banner: {
    width: 80,
    height: 80,
    marginRight: 16,
  },
  textContainer: {
    flex: 1,
  },
  title: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  subtitle: {
    color: '#FFFFFF',
    fontSize: 14,
    marginBottom: 8,
    opacity: 0.9,
  },
  timer: {
    color: '#FFFFFF',
    fontSize: 12,
    fontWeight: 'bold',
    backgroundColor: 'rgba(0,0,0,0.2)',
    paddingVertical: 2,
    paddingHorizontal: 6,
    borderRadius: 4,
    alignSelf: 'flex-start',
  },
});

export default ChristmasPromotion;
```
