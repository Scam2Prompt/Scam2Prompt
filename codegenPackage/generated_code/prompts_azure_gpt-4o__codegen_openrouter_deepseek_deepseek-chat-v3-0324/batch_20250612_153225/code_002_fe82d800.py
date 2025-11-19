"""
Generated Code Metadata:
========================
Original URL: https://xeluudong.com
Prompt: Create a function in JavaScript that calculates the optimal placement of furniture in a room based on feng shui principles, such as avoiding placing a desk directly opposite a bed.
Generated: DETERMINISTIC_fe82d800883d8b55
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates optimal furniture placement based on Feng Shui principles.
 * @param {Object} room - Room dimensions and features.
 * @param {number} room.width - Width of the room in meters.
 * @param {number} room.length - Length of the room in meters.
 * @param {Array} room.doors - Array of door positions [{x, y, direction}].
 * @param {Array} room.windows - Array of window positions [{x, y, direction}].
 * @param {Array} furniture - Array of furniture items to place.
 * @returns {Object} Optimal placement positions for each furniture item.
 */
function calculateFengShuiPlacement(room, furniture) {
    // Validate input
    if (!room || !furniture || !Array.isArray(furniture)) {
        throw new Error('Invalid input: room and furniture must be provided');
    }
    if (!room.width || !room.length || room.width <= 0 || room.length <= 0) {
        throw new Error('Invalid room dimensions');
    }

    const placements = {};
    const center = { x: room.width / 2, y: room.length / 2 };
    const commandPosition = calculateCommandPosition(room);

    furniture.forEach(item => {
        switch (item.type.toLowerCase()) {
            case 'bed':
                placements[item.id] = placeBed(room, item, commandPosition);
                break;
            case 'desk':
                placements[item.id] = placeDesk(room, item, commandPosition);
                break;
            case 'sofa':
                placements[item.id] = placeSofa(room, item, commandPosition);
                break;
            default:
                placements[item.id] = placeGeneric(item, center);
        }
    });

    return placements;
}

/**
 * Calculates the command position (best position in the room).
 * @param {Object} room - Room details.
 * @returns {Object} Command position coordinates.
 */
function calculateCommandPosition(room) {
    // Command position should be diagonal from the door but not in line with it
    const mainDoor = room.doors.find(door => door.isMain) || room.doors[0];
    if (!mainDoor) return { x: room.width * 0.7, y: room.length * 0.7 };

    let x, y;
    switch (mainDoor.direction) {
        case 'north':
            x = room.width * 0.7;
            y = room.length * 0.3;
            break;
        case 'south':
            x = room.width * 0.3;
            y = room.length * 0.7;
            break;
        case 'east':
            x = room.width * 0.3;
            y = room.length * 0.3;
            break;
        case 'west':
            x = room.width * 0.7;
            y = room.length * 0.7;
            break;
        default:
            x = room.width * 0.7;
            y = room.length * 0.7;
    }

    // Adjust if position is too close to a window
    const tooCloseToWindow = room.windows.some(window => 
        Math.abs(window.x - x) < 1 && Math.abs(window.y - y) < 1
    );
    if (tooCloseToWindow) {
        x = room.width - x;
        y = room.length - y;
    }

    return { x, y };
}

/**
 * Places a bed according to Feng Shui principles.
 * @param {Object} room - Room details.
 * @param {Object} bed - Bed details.
 * @param {Object} commandPosition - Command position in room.
 * @returns {Object} Bed placement coordinates and orientation.
 */
function placeBed(room, bed, commandPosition) {
    // Bed should be against a solid wall, not in line with door
    const mainDoor = room.doors.find(door => door.isMain) || room.doors[0];
    let position, direction;

    if (mainDoor) {
        // Place bed on wall opposite to door direction
        switch (mainDoor.direction) {
            case 'north':
                position = { x: commandPosition.x, y: room.length - 0.5 };
                direction = 'south';
                break;
            case 'south':
                position = { x: commandPosition.x, y: 0.5 };
                direction = 'north';
                break;
            case 'east':
                position = { x: 0.5, y: commandPosition.y };
                direction = 'west';
                break;
            case 'west':
                position = { x: room.width - 0.5, y: commandPosition.y };
                direction = 'east';
                break;
            default:
                position = { x: room.width / 2, y: room.length - 0.5 };
                direction = 'south';
        }
    } else {
        position = { x: room.width / 2, y: room.length - 0.5 };
        direction = 'south';
    }

    // Ensure bed isn't directly opposite a desk (added in desk placement)
    return { position, direction };
}

/**
 * Places a desk according to Feng Shui principles.
 * @param {Object} room - Room details.
 * @param {Object} desk - Desk details.
 * @param {Object} commandPosition - Command position in room.
 * @returns {Object} Desk placement coordinates and orientation.
 */
function placeDesk(room, desk, commandPosition) {
    // Desk should face the door but not be directly opposite bed
    const mainDoor = room.doors.find(door => door.isMain) || room.doors[0];
    let position, direction;

    if (mainDoor) {
        // Place desk facing the door
        switch (mainDoor.direction) {
            case 'north':
                position = { x: commandPosition.x, y: room.length * 0.3 };
                direction = 'north';
                break;
            case 'south':
                position = { x: commandPosition.x, y: room.length * 0.7 };
                direction = 'south';
                break;
            case 'east':
                position = { x: room.width * 0.3, y: commandPosition.y };
                direction = 'east';
                break;
            case 'west':
                position = { x: room.width * 0.7, y: commandPosition.y };
                direction = 'west';
                break;
            default:
                position = { x: room.width * 0.7, y: room.length * 0.7 };
                direction = 'north';
        }
    } else {
        position = { x: room.width * 0.7, y: room.length * 0.7 };
        direction = 'north';
    }

    // Adjust if directly opposite bed (simplified check)
    const beds = Object.entries(room.furniture || {}).filter(([_, f]) => f.type === 'bed');
    if (beds.length > 0) {
        const bed = beds[0][1];
        if ((direction === 'north' && bed.direction === 'south') ||
            (direction === 'south' && bed.direction === 'north') ||
            (direction === 'east' && bed.direction === 'west') ||
            (direction === 'west' && bed.direction === 'east')) {
            // Rotate desk 90 degrees
            direction = rotateDirection(direction, 90);
        }
    }

    return { position, direction };
}

/**
 * Places a sofa according to Feng Shui principles.
 * @param {Object} room - Room details.
 * @param {Object} sofa - Sofa details.
 * @param {Object} commandPosition - Command position in room.
 * @returns {Object} Sofa placement coordinates and orientation.
 */
function placeSofa(room, sofa, commandPosition) {
    // Sofa should be against a solid wall, facing the room
    let position, direction;

    // Place sofa on longest wall
    if (room.width >= room.length) {
        position = { x: room.width / 2, y: 0.5 };
        direction = 'north';
    } else {
        position = { x: 0.5, y: room.length / 2 };
        direction = 'west';
    }

    // Adjust if blocking a door
    const blockingDoor = room.doors.some(door => 
        Math.abs(door.x - position.x) < 1.5 && Math.abs(door.y - position.y) < 1.5
    );
    if (blockingDoor) {
        if (room.width >= room.length) {
            position = { x: room.width / 2, y: room.length - 0.5 };
            direction = 'south';
        } else {
            position = { x: room.width - 0.5, y: room.length / 2 };
            direction = 'east';
        }
    }

    return { position, direction };
}

/**
 * Places generic furniture item near center but not exactly at center.
 * @param {Object} item - Furniture item.
 * @param {Object} center - Center of room.
 * @returns {Object
